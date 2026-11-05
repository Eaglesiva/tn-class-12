import os, sys, json, time, requests, fitz, hashlib, subprocess, re

sys.stdout.reconfigure(encoding='utf-8')

print("=================================================================")
print("SCERT 2026-27 - OFFICIAL PDF DIRECT REFRESH: CLASS 12 (32 BOOKS)")
print("=================================================================")

TARGET_BOOKS = [
  {
    "class": "12",
    "subject": "General Tamil",
    "medium": "Tamil",
    "filename": "12th_Genreal%20Tamil.pdf",
    "official_url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/12th_Genreal%20Tamil.pdf",
    "expected_pages": 240,
    "local_folder": "tamil",
    "slug": "tamil"
  },
  {
    "class": "12",
    "subject": "General English",
    "medium": "English",
    "filename": "12th_General%20English_Text.pdf",
    "official_url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/12th_General%20English_Text.pdf",
    "expected_pages": 248,
    "local_folder": "english",
    "slug": "english"
  },
  {
    "class": "12",
    "subject": "Mathematics (Vol I)",
    "medium": "Tamil",
    "filename": "12th_Maths_Vol-1_Tamil%20Medium_Text.pdf",
    "official_url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/12th_Maths_Vol-1_Tamil%20Medium_Text.pdf",
    "expected_pages": 336,
    "local_folder": "maths_tm",
    "slug": "maths_tm_vol1"
  },
  {
    "class": "12",
    "subject": "Mathematics (Vol II)",
    "medium": "Tamil",
    "filename": "12th_Maths_Vol-2_Tamil%20Meduim_Text.pdf",
    "official_url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/12th_Maths_Vol-2_Tamil%20Meduim_Text.pdf",
    "expected_pages": 288,
    "local_folder": "maths_tm",
    "slug": "maths_tm_vol2"
  },
  {
    "class": "12",
    "subject": "Mathematics (Vol I)",
    "medium": "English",
    "filename": "12th_Maths_Vol-1_English%20Meduim_Text.pdf",
    "official_url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/12th_Maths_Vol-1_English%20Meduim_Text.pdf",
    "expected_pages": 304,
    "local_folder": "maths_em",
    "slug": "maths_em_vol1"
  },
  {
    "class": "12",
    "subject": "Mathematics (Vol II)",
    "medium": "English",
    "filename": "12th_Maths_Vol-2_English%20Meduim_Text.pdf",
    "official_url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/12th_Maths_Vol-2_English%20Meduim_Text.pdf",
    "expected_pages": 272,
    "local_folder": "maths_em",
    "slug": "maths_em_vol2"
  },
  {
    "class": "12",
    "subject": "Physics (Vol I)",
    "medium": "Tamil",
    "filename": "12th_Physics_Vol-1_Tamil%20Medium_Text.pdf",
    "official_url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/12th_Physics_Vol-1_Tamil%20Medium_Text.pdf",
    "expected_pages": 352,
    "local_folder": "physics_tm",
    "slug": "physics_tm_vol1"
  },
  {
    "class": "12",
    "subject": "Physics (Vol II)",
    "medium": "Tamil",
    "filename": "12th_Physics_Vol-2_Tamil%20Medium_Text.pdf",
    "official_url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/12th_Physics_Vol-2_Tamil%20Medium_Text.pdf",
    "expected_pages": 312,
    "local_folder": "physics_tm",
    "slug": "physics_tm_vol2"
  },
  {
    "class": "12",
    "subject": "Physics (Vol II)",
    "medium": "English",
    "filename": "12th_Physics_Vol-2_English%20Medium_Text.pdf",
    "official_url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/12th_Physics_Vol-2_English%20Medium_Text.pdf",
    "expected_pages": 296,
    "local_folder": "physics_em",
    "slug": "physics_em_vol2"
  },
  {
    "class": "12",
    "subject": "Chemistry (Vol I)",
    "medium": "Tamil",
    "filename": "12th_Chemistry-Vol-1_Tamil%20Medium_Text.pdf",
    "official_url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/12th_Chemistry-Vol-1_Tamil%20Medium_Text.pdf",
    "expected_pages": 328,
    "local_folder": "chemistry_tm",
    "slug": "chemistry_tm_vol1"
  },
  {
    "class": "12",
    "subject": "Chemistry (Vol II)",
    "medium": "Tamil",
    "filename": "12th_Chemistry-Vol-2_Tamil%20Medium_Text.pdf",
    "official_url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/12th_Chemistry-Vol-2_Tamil%20Medium_Text.pdf",
    "expected_pages": 344,
    "local_folder": "chemistry_tm",
    "slug": "chemistry_tm_vol2"
  },
  {
    "class": "12",
    "subject": "Chemistry (Vol II)",
    "medium": "English",
    "filename": "12th_Chemistry-Vol-2_English%20Medium_Text.pdf",
    "official_url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/12th_Chemistry-Vol-2_English%20Medium_Text.pdf",
    "expected_pages": 328,
    "local_folder": "chemistry_em",
    "slug": "chemistry_em_vol2"
  },
  {
    "class": "12",
    "subject": "Botany",
    "medium": "Tamil",
    "filename": "12th_Botany_TM_Text.pdf",
    "official_url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/12th_Botany_TM_Text.pdf",
    "expected_pages": 336,
    "local_folder": "botany_tm",
    "slug": "botany_tm"
  },
  {
    "class": "12",
    "subject": "Botany",
    "medium": "English",
    "filename": "12th_Botany_EM_Text.pdf",
    "official_url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/12th_Botany_EM_Text.pdf",
    "expected_pages": 312,
    "local_folder": "botany_em",
    "slug": "botany_em"
  },
  {
    "class": "12",
    "subject": "Zoology",
    "medium": "Tamil",
    "filename": "12th_Zoology_TM_Text.pdf",
    "official_url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/12th_Zoology_TM_Text.pdf",
    "expected_pages": 336,
    "local_folder": "zoology_tm",
    "slug": "zoology_tm"
  },
  {
    "class": "12",
    "subject": "Zoology",
    "medium": "English",
    "filename": "12th_Zoology_EM_Text.pdf",
    "official_url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/12th_Zoology_EM_Text.pdf",
    "expected_pages": 280,
    "local_folder": "zoology_em",
    "slug": "zoology_em"
  },
  {
    "class": "12",
    "subject": "Bio-Zoology",
    "medium": "Tamil",
    "filename": "12th_Bio-Zoology_TM_Text.pdf",
    "official_url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/12th_Bio-Zoology_TM_Text.pdf",
    "expected_pages": 312,
    "local_folder": "bio_zoology_tm",
    "slug": "bio_zoology_tm"
  },
  {
    "class": "12",
    "subject": "Bio-Zoology",
    "medium": "English",
    "filename": "12th_Bio-Zoology_EM_Text.pdf",
    "official_url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/12th_Bio-Zoology_EM_Text.pdf",
    "expected_pages": 264,
    "local_folder": "bio_zoology_em",
    "slug": "bio_zoology_em"
  },
  {
    "class": "12",
    "subject": "Computer Science",
    "medium": "Tamil",
    "filename": "12th_Computer%20Science_TM_Text.pdf",
    "official_url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/12th_Computer%20Science_TM_Text.pdf",
    "expected_pages": 360,
    "local_folder": "computer_science_tm",
    "slug": "computer_science_tm"
  },
  {
    "class": "12",
    "subject": "Computer Science",
    "medium": "English",
    "filename": "12th_Computer%20Science_EM_Text.pdf",
    "official_url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/12th_Computer%20Science_EM_Text.pdf",
    "expected_pages": 360,
    "local_folder": "computer_science_em",
    "slug": "computer_science_em"
  },
  {
    "class": "12",
    "subject": "Commerce",
    "medium": "Tamil",
    "filename": "12th_Commerce_TM_Text.pdf",
    "official_url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/12th_Commerce_TM_Text.pdf",
    "expected_pages": 288,
    "local_folder": "commerce_tm",
    "slug": "commerce_tm"
  },
  {
    "class": "12",
    "subject": "Commerce",
    "medium": "English",
    "filename": "12th_Commerce_EM_Text.pdf",
    "official_url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/12th_Commerce_EM_Text.pdf",
    "expected_pages": 288,
    "local_folder": "commerce_em",
    "slug": "commerce_em"
  },
  {
    "class": "12",
    "subject": "Accountancy",
    "medium": "Tamil",
    "filename": "12th_Accountancy_TM_Text.pdf",
    "official_url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/12th_Accountancy_TM_Text.pdf",
    "expected_pages": 368,
    "local_folder": "accountancy_tm",
    "slug": "accountancy_tm"
  },
  {
    "class": "12",
    "subject": "Accountancy",
    "medium": "English",
    "filename": "12th_Accountancy_EM_Text.pdf",
    "official_url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/12th_Accountancy_EM_Text.pdf",
    "expected_pages": 368,
    "local_folder": "accountancy_em",
    "slug": "accountancy_em"
  },
  {
    "class": "12",
    "subject": "Economics",
    "medium": "Tamil",
    "filename": "12th_Economics_TM_Text.pdf",
    "official_url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/12th_Economics_TM_Text.pdf",
    "expected_pages": 336,
    "local_folder": "economics_tm",
    "slug": "economics_tm"
  },
  {
    "class": "12",
    "subject": "Economics",
    "medium": "English",
    "filename": "12th_Economics_EM_Text.pdf",
    "official_url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/12th_Economics_EM_Text.pdf",
    "expected_pages": 296,
    "local_folder": "economics_em",
    "slug": "economics_em"
  },
  {
    "class": "12",
    "subject": "History",
    "medium": "Tamil",
    "filename": "12th_History_TM_Text.pdf",
    "official_url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/12th_History_TM_Text.pdf",
    "expected_pages": 312,
    "local_folder": "history_tm",
    "slug": "history_tm"
  },
  {
    "class": "12",
    "subject": "History",
    "medium": "English",
    "filename": "12th_History_EM_Text.pdf",
    "official_url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/12th_History_EM_Text.pdf",
    "expected_pages": 272,
    "local_folder": "history_em",
    "slug": "history_em"
  },
  {
    "class": "12",
    "subject": "Geography",
    "medium": "Tamil",
    "filename": "12th_Geography_TM_Text.pdf",
    "official_url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/12th_Geography_TM_Text.pdf",
    "expected_pages": 232,
    "local_folder": "geography_tm",
    "slug": "geography_tm"
  },
  {
    "class": "12",
    "subject": "Geography",
    "medium": "English",
    "filename": "12th_Geography_EM_Text.pdf",
    "official_url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/12th_Geography_EM_Text.pdf",
    "expected_pages": 216,
    "local_folder": "geography_em",
    "slug": "geography_em"
  },
  {
    "class": "12",
    "subject": "Political Science",
    "medium": "Tamil",
    "filename": "12th_Political%20Science%20TM_Text.pdf",
    "official_url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/12th_Political%20Science%20TM_Text.pdf",
    "expected_pages": 360,
    "local_folder": "political_science_tm",
    "slug": "political_science_tm"
  },
  {
    "class": "12",
    "subject": "Political Science",
    "medium": "English",
    "filename": "12th_Political%20Science%20EM_Text.pdf",
    "official_url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/12th_Political%20Science%20EM_Text.pdf",
    "expected_pages": 328,
    "local_folder": "political_science_em",
    "slug": "political_science_em"
  }
]

def get_existing_paths_for_book(t, all_pdf_paths):
    folder = t['local_folder']
    fn = t['filename']
    
    # 1. Maths TM & EM
    if folder in ['maths_tm', 'maths_em']:
        vol = 'vol1' if 'Vol-1' in fn else 'vol2'
        return [p for p in all_pdf_paths if p.startswith(f"{folder}/{vol}/")]
        
    # 2. Physics TM
    if folder == 'physics_tm':
        if 'Vol-1' in fn:
            vol1_prefixes = tuple(f"physics_tm/{d:02d}_" for d in range(9))
            return [p for p in all_pdf_paths if p.startswith(vol1_prefixes)]
        else:
            vol2_prefixes = tuple(f"physics_tm/{d:02d}_" for d in range(9, 17))
            return [p for p in all_pdf_paths if p.startswith(vol2_prefixes)]

    # 3. Physics EM
    if folder == 'physics_em':
        vol2_prefixes = tuple(f"physics_em/{d:02d}_" for d in range(9, 17))
        return [p for p in all_pdf_paths if p.startswith(vol2_prefixes)]

    # 4. Chemistry TM
    if folder == 'chemistry_tm':
        if 'Vol-1' in fn:
            vol1_prefixes = tuple(f"chemistry_tm/{d:02d}_" for d in range(11))
            return [p for p in all_pdf_paths if p.startswith(vol1_prefixes)]
        else:
            vol2_prefixes = tuple(f"chemistry_tm/{d:02d}_" for d in range(11, 22))
            return [p for p in all_pdf_paths if p.startswith(vol2_prefixes)]

    # 5. Chemistry EM
    if folder == 'chemistry_em':
        vol2_prefixes = tuple(f"chemistry_em/{d:02d}_" for d in range(11, 22))
        return [p for p in all_pdf_paths if p.startswith(vol2_prefixes)]

    # 6. Single volume books
    return [p for p in all_pdf_paths if p.startswith(folder + '/')]

os.makedirs('docs/refresh_evidence', exist_ok=True)
all_evidence = []

# Git author config
subprocess.run(['git', 'config', 'user.name', 'github-actions[bot]'])
subprocess.run(['git', 'config', 'user.email', 'github-actions[bot]@users.noreply.github.com'])

# Get all pdf files in repo
p_ls = subprocess.run(['git', 'ls-files'], capture_output=True, text=True)
all_pdf_paths = [p.replace('\\', '/').strip() for p in p_ls.stdout.splitlines() if p.strip().endswith('.pdf')]
if not all_pdf_paths:
    for root, _, files in os.walk('.'):
        for f in files:
            if f.endswith('.pdf'):
                all_pdf_paths.append(os.path.relpath(os.path.join(root, f), '.').replace('\\', '/'))

print(f"Total existing PDF files discovered: {len(all_pdf_paths)}")

branch_name = os.environ.get('GITHUB_REF_NAME', 'scert/refresh/class-12')
print(f"Target Branch: {branch_name}")

for idx, b in enumerate(TARGET_BOOKS, 1):
    slug = b['slug']
    print(f"\n=======================================================")
    print(f"[{idx:02d}/32] PROCESSING: {b['subject']} ({b['medium']}) - {b['expected_pages']}p [Slug: {slug}]")
    print(f"URL: {b['official_url']}")
    print(f"Folder: {b['local_folder']}")
    print(f"=======================================================")
    
    # 1. Identify existing page PDF paths
    matched_pages = get_existing_paths_for_book(b, all_pdf_paths)
    matched_pages.sort()
    print(f"Existing page PDF count: {len(matched_pages)} (Expected: {b['expected_pages']})")
    
    if len(matched_pages) != b['expected_pages']:
        print(f"ERROR: Page count mismatch in repository! Found {len(matched_pages)} != {b['expected_pages']}. Skipping book.")
        continue
        
    # 2. Download Official Master PDF to /tmp
    temp_pdf_path = f"/tmp/master_c12_{slug}.pdf"
    print(f"Downloading master PDF to {temp_pdf_path}...")
    t0 = time.time()
    
    try:
        resp = requests.get(b['official_url'], headers={'User-Agent': 'Mozilla/5.0'}, stream=True, timeout=180)
        resp.raise_for_status()
    except Exception as e:
        print(f"ERROR: Download failed: {e}. Skipping book.")
        continue
        
    content_length = int(resp.headers.get('Content-Length', 0))
    etag = resp.headers.get('ETag', '').strip('"')
    last_modified = resp.headers.get('Last-Modified', '')
    
    sha256 = hashlib.sha256()
    with open(temp_pdf_path, 'wb') as f:
        for chunk in resp.iter_content(chunk_size=1024*1024):
            if chunk:
                f.write(chunk)
                sha256.update(chunk)
                
    master_sha256 = sha256.hexdigest()
    master_size = os.path.getsize(temp_pdf_path)
    elapsed = time.time() - t0
    print(f"Downloaded {master_size} bytes in {elapsed:.2f}s | SHA-256: {master_sha256}")
    
    # Magic bytes check
    with open(temp_pdf_path, 'rb') as f:
        magic = f.read(5)
    if not magic.startswith(b'%PDF'):
        print(f"ERROR: Invalid PDF magic bytes: {magic}. Skipping book.")
        if os.path.exists(temp_pdf_path):
            os.remove(temp_pdf_path)
        continue
        
    # 3. Open PyMuPDF and Validate Page Count
    doc = fitz.open(temp_pdf_path)
    master_page_count = len(doc)
    print(f"Master PDF Page Count: {master_page_count}")
    
    if master_page_count != b['expected_pages']:
        print(f"ERROR: Master page count {master_page_count} != Expected {b['expected_pages']}. Skipping book.")
        doc.close()
        if os.path.exists(temp_pdf_path):
            os.remove(temp_pdf_path)
        continue
        
    # 4. In-Place Single-Page PDF Splitting & Overwrite
    print(f"Splitting master PDF and overwriting {master_page_count} pages...")
    split_success_count = 0
    for p_idx in range(master_page_count):
        dest_page_path = matched_pages[p_idx]
        single_doc = fitz.open()
        single_doc.insert_pdf(doc, from_page=p_idx, to_page=p_idx)
        single_doc.save(dest_page_path)
        single_doc.close()
        
        # Validation
        check_doc = fitz.open(dest_page_path)
        if len(check_doc) != 1 or os.path.getsize(dest_page_path) == 0:
            print(f"FAILED validation on {dest_page_path}!")
            check_doc.close()
            doc.close()
            sys.exit(1)
        check_doc.close()
        split_success_count += 1
        
    print(f"Successfully split and validated {split_success_count} / {master_page_count} pages.")
    
    # 5. Delete temporary master PDF immediately (Zero Local Master PDF Persistence)
    doc.close()
    if os.path.exists(temp_pdf_path):
        os.remove(temp_pdf_path)
        print("Zero Local Master PDF Persistence: /tmp master PDF removed.")
        
    # 6. Verify Git Safety & Restore any untouched non-PDF files
    p_status = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
    for line in p_status.stdout.splitlines():
        parts = line.strip().split(maxsplit=1)
        if len(parts) == 2:
            fpath = parts[1]
            if not fpath.endswith('.pdf') and not fpath.startswith('.github/') and not fpath.startswith('docs/refresh_evidence/'):
                subprocess.run(['git', 'checkout', '--', fpath])
                print(f"Restored untouched non-pdf file: {fpath}")
                
    # 7. Write Evidence Record
    evidence = {
        'book_id': f"class_12_{slug}",
        'class': '12',
        'subject': b['subject'],
        'medium': b['medium'],
        'official_filename': b['filename'],
        'official_url': b['official_url'],
        'http_status': 'GET_200',
        'content_length': master_size,
        'etag': etag,
        'last_modified': last_modified,
        'sha256': master_sha256,
        'expected_page_count': b['expected_pages'],
        'actual_page_count': master_page_count,
        'pages_replaced_count': split_success_count,
        'all_pages_validated': True,
        'refresh_status': 'OFFICIAL_SOURCE_REFRESHED',
        'timestamp_utc': time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        'zero_master_pdf_persistence_verified': True
    }
    
    ev_path = f"docs/refresh_evidence/class_12_{slug}_refresh_evidence.json"
    with open(ev_path, 'w', encoding='utf-8') as f_ev:
        json.dump(evidence, f_ev, indent=2)
    all_evidence.append(evidence)
    
    # 8. Git Commit & Push for This Book
    print(f"Committing changes for {b['subject']} ({b['medium']})...")
    for i in range(0, len(matched_pages), 100):
        subprocess.run(['git', 'add'] + matched_pages[i:i+100])
    subprocess.run(['git', 'add', ev_path])
    commit_msg = f"feat(scert): refresh official PDF pages for {b['subject']} ({b['medium']}) [{split_success_count} pages]"
    subprocess.run(['git', 'commit', '-m', commit_msg])
    
    # Push progress
    p_push = subprocess.run(['git', 'push', 'origin', f"HEAD:{branch_name}"])
    if p_push.returncode == 0:
        print(f"Progress pushed to remote branch {branch_name} successfully.")
    else:
        print(f"Warning: incremental push returned {p_push.returncode}, will push at end.")

# Final summary evidence
with open('docs/refresh_evidence/class_12_all_refreshed_evidence.json', 'w', encoding='utf-8') as f_all:
    json.dump(all_evidence, f_all, indent=2)

subprocess.run(['git', 'add', 'docs/refresh_evidence/class_12_all_refreshed_evidence.json'])
subprocess.run(['git', 'commit', '-m', f"docs(scert): finalize all Class 12 refresh evidence records ({len(all_evidence)}/32 books)"])
subprocess.run(['git', 'push', 'origin', f"HEAD:{branch_name}"])

print("\n=======================================================")
print(f"Class 12 Refresh Completed: {len(all_evidence)} / 32 books successfully refreshed and committed!")
print("=======================================================")
