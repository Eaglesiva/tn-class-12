import os, sys, json, time, requests, fitz, hashlib

print("=== Starting Class 12 Cloud Edition Update Job ===")

books = [
    {
        "key": "physics_em_vol1",
        "subject_dir": "physics_em",
        "vol_dir": "vol1",
        "name": "Physics (Vol I)",
        "medium": "English",
        "url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/12th_Physics_Vol-1_English%20Medium_Text.pdf",
        "edition_name": "2026-27-scert-official"
    },
    {
        "key": "chemistry_em_vol1",
        "subject_dir": "chemistry_em",
        "vol_dir": "vol1",
        "name": "Chemistry (Vol I)",
        "medium": "English",
        "url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/12th_Chemistry_Vol-1_EM_Text.pdf",
        "edition_name": "2026-27-scert-official"
    }
]

summary_results = []

for b in books:
    print(f"\n=======================================================")
    print(f"Processing: {b['name']} ({b['medium']})")
    print(f"Official URL: {b['url']}")
    
    # 1. Download Master PDF to Runner temp file
    temp_pdf = f"runner_temp_{b['key']}.pdf"
    print(f"Downloading master to {temp_pdf}...")
    resp = requests.get(b['url'], headers={'User-Agent': 'Mozilla/5.0'}, stream=True)
    resp.raise_for_status()
    with open(temp_pdf, 'wb') as f:
        for chunk in resp.iter_content(chunk_size=1024*1024):
            if chunk:
                f.write(chunk)
                
    file_size_mb = os.path.getsize(temp_pdf) / (1024*1024)
    print(f"Downloaded master PDF: {file_size_mb:.2f} MB")
    
    # 2. Inspect Page 2 & Total Page Count
    doc = fitz.open(temp_pdf)
    total_pages = len(doc)
    p2_text = doc[1].get_text() if total_pages >= 2 else ""
    p2_lines = [l.strip() for l in p2_text.splitlines() if l.strip()]
    imprint_lines = [l for l in p2_lines if any(yr in l for yr in ['2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', 'First', 'Revised', 'Reprint', 'பதிப்பு'])]
    print(f"Total pages: {total_pages}")
    print(f"Page 2 Imprint: {' | '.join(imprint_lines)}")
    
    # 3. Create Edition folder structure
    # physics_em/editions/2026-27-scert-official/vol1/
    #   edition.json
    #   edition.md
    #   pages.json
    #   manifest.json
    #   pages/page_001.pdf ...
    ed_base = os.path.join(b['subject_dir'], "editions", b['edition_name'], b['vol_dir'])
    pages_dir = os.path.join(ed_base, "pages")
    os.makedirs(pages_dir, exist_ok=True)
    
    # 4. Split PDF into single pages
    print(f"Splitting {total_pages} pages into {pages_dir}...")
    manifest_entries = []
    page_files = []
    
    for p_idx in range(total_pages):
        single_doc = fitz.open()
        single_doc.insert_pdf(doc, from_page=p_idx, to_page=p_idx)
        p_filename = f"page_{p_idx + 1:03d}.pdf"
        p_path = os.path.join(pages_dir, p_filename)
        single_doc.save(p_path)
        single_doc.close()
        
        # Calculate SHA256 of single page
        h = hashlib.sha256()
        with open(p_path, 'rb') as pf:
            h.update(pf.read())
        sha256 = h.hexdigest()
        
        page_files.append(f"./pages/{p_filename}")
        manifest_entries.append({
            "page_number": p_idx + 1,
            "filename": p_filename,
            "rel_path": f"pages/{p_filename}",
            "sha256": sha256,
            "size_bytes": os.path.getsize(p_path)
        })
        
        if (p_idx + 1) % 50 == 0 or (p_idx + 1) == total_pages:
            print(f"  Split progress: {p_idx + 1}/{total_pages}")
            
    doc.close()
    
    # Clean up large master PDF immediately
    if os.path.exists(temp_pdf):
        os.remove(temp_pdf)
    print("Master PDF deleted from runner storage.")
    
    # 5. Write pages.json, manifest.json, edition.json, edition.md
    with open(os.path.join(ed_base, "pages.json"), "w", encoding="utf-8") as f:
        json.dump(page_files, f, indent=2)
        
    with open(os.path.join(ed_base, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump({
            "subject": b["name"],
            "medium": b["medium"],
            "edition_name": b["edition_name"],
            "volume": b["vol_dir"],
            "total_pages": total_pages,
            "master_url": b["url"],
            "pages": manifest_entries
        }, f, indent=2)
        
    edition_meta = {
        "subject_name": b["name"],
        "medium": b["medium"],
        "volume": b["vol_dir"],
        "edition_name": b["edition_name"],
        "source_url": b["url"],
        "download_date": time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime()),
        "total_pages": total_pages,
        "imprint_lines": imprint_lines,
        "runner_os": sys.platform
    }
    with open(os.path.join(ed_base, "edition.json"), "w", encoding="utf-8") as f:
        json.dump(edition_meta, f, indent=2)
        
    with open(os.path.join(ed_base, "edition.md"), "w", encoding="utf-8") as f:
        f.write(f"# Official SCERT Edition: {b['name']} ({b['medium']})\n\n")
        f.write(f"- **Edition Tag**: `{b['edition_name']}`\n")
        f.write(f"- **Volume**: `{b['vol_dir']}`\n")
        f.write(f"- **Official URL**: {b['url']}\n")
        f.write(f"- **Download Timestamp**: {edition_meta['download_date']}\n")
        f.write(f"- **Total Page Count**: {total_pages}\n")
        f.write(f"- **Page 2 Imprint**:\n")
        for line in imprint_lines:
            f.write(f"  - {line}\n")
            
    print(f"Edition metadata saved in {ed_base}")
    summary_results.append({
        "key": b["key"],
        "name": b["name"],
        "medium": b["medium"],
        "total_pages": total_pages,
        "edition_dir": ed_base
    })

# Save job summary report
os.makedirs("docs", exist_ok=True)
with open("docs/class_12_cloud_edition_update_report.md", "w", encoding="utf-8") as f:
    f.write("# Class 12 Cloud Edition Update Report\n\n")
    f.write("Generated automatically via GitHub Actions Cloud-Only Runner.\n\n")
    f.write("| Subject | Medium | Total Pages | Edition Directory |\n")
    f.write("| :--- | :---: | :---: | :--- |\n")
    for s in summary_results:
        f.write(f"| {s['name']} | {s['medium']} | {s['total_pages']} | `{s['edition_dir']}` |\n")

print("\n=== All 2 Class 12 Books Processed Successfully in Cloud Runner ===")
