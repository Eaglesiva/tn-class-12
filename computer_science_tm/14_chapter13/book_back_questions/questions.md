# Standard 12 Computer Science (தமிழ் வழி) - அத்தியாயம் 13: பைத்தான் மற்றும் CSV கோப்புகள்
## Book-Back Evaluation Questions (Questions Only)

> **பாடநூல் அச்சிடப்பட்ட பக்கங்கள்:** 262 – 265  
> **Source HTML Links:**
> - [பக்கம் 262 HTML](file:///e:/19.03.26/new%20project/tn_school_books/12th/computer_science_tm/full_book/04_tharavuthtalakk_karuthurukkal_mysql/03_python_matrum_csv_goppugal/page_262/page_262.html)
> - [பக்கம் 263 HTML](file:///e:/19.03.26/new%20project/tn_school_books/12th/computer_science_tm/full_book/04_tharavuthtalakk_karuthurukkal_mysql/03_python_matrum_csv_goppugal/page_263/page_263.html)
> - [பக்கம் 264 HTML](file:///e:/19.03.26/new%20project/tn_school_books/12th/computer_science_tm/full_book/04_tharavuthtalakk_karuthurukkal_mysql/03_python_matrum_csv_goppugal/page_264/page_264.html)
> - [பக்கம் 265 HTML](file:///e:/19.03.26/new%20project/tn_school_books/12th/computer_science_tm/full_book/04_tharavuthtalakk_karuthurukkal_mysql/03_python_matrum_csv_goppugal/page_265/page_265.html)

---

### செய்முறைப் பயிற்சி

1. `Namelist.csv` கோப்பை படித்து அதில் உள்ள பெயர் புலத்தில் வரிசையாக்கம் செய்து அதை list-ல் எழுதி வெளியீடு செய்வதற்கான பைத்தான் நிரல் எழுதுக:

   | SNO | NAME | OCCUPATION |
   | :--- | :--- | :--- |
   | 1 | NIVETHITHA | ENGINEER |
   | 2 | ADHITH | DOCTOR |
   | 3 | LAVANYA | SINGER |
   | 4 | VIDHYA | TEACHER |
   | 5 | BINDHU | LECTURER |

2. ஐந்து மாணவர்களின் ஐந்து பாடத்தின் மதிப்பெண்களை மாணவரின் பெயருடன் உள்ளீடு செய்ய பைத்தான் நிரலை எழுதுக. மேலும் மதிப்பெண்ணின் கூட்டுத்தொகையை கண்டறிந்து எல்லா விவரங்களையும் CSV கோப்பில் எழுதுக.

---

### பகுதி - அ: சரியான விடையைத் தேர்ந்தெடுத்து எழுதுக (1 மதிப்பெண்)

1. CSV கோப்பானது பின்வருவனவற்றுள் எவ்வாறு அழைக்கப்பட்டுள்ளது?
   அ) Flat File
   ஆ) 3D File
   இ) String File
   ஈ) Random File

2. CRLF என்பதன் விரிவாக்கம்
   அ) Control Return and Line Feed
   ஆ) Carriage Return and Form Feed
   இ) Control Router and Line Feed
   ஈ) Carriage Return and Line Feed

3. பின்வருவனவற்றுள் எந்த தொகுதியானது CSV கோப்பினில் பல்வேறு செயல்பாடுகளை செய்ய பைத்தானால் வழங்கப்பட்டுள்ளது?
   அ) py
   ஆ) xls
   இ) csv
   ஈ) os

4. உருவப்படம் அல்லது இயங்குநிலை கோப்பு போன்று உரை அல்லாத கோப்புகளை கையாள பின்வரும் எந்த முறைமையானது பயன்படுகிறது?
   அ) உரை (Text mode)
   ஆ) இருமநிலை (Binary mode)
   இ) xls
   ஈ) csv

5. கோப்பினில் ஒரு வரிசையை தவிர்க்க பயன்படும் கட்டளை:
   அ) next()
   ஆ) skip()
   இ) omit()
   ஈ) bounce()

6. பின்வருவனவற்றுள் CSV தொகுதியில் `writer()` முறையால் வழங்கப்பட்டுள்ள வரிமுறிப்பான் எது?
   அ) Line Terminator
   ஆ) Enter key
   இ) Form feed
   ஈ) Data Terminator

7. பின்வரும் நிரலின் வெளியீடு யாது? "city.csv" என்ற கோப்பில் கீழேயுள்ள விவரங்களை கொண்டிருப்பின்:
   ```
   chennai,mylapore
   mumbai,andheri
   ```
   ```python
   import csv
   d=csv.reader(open("city.csv"))
   next(d)
   for row in d:
       print(row)
   ```
   அ) `['chennai', 'mylapore']`  
   ஆ) `['mumbai', 'andheri']`  
   இ) `['chennai']`  
   ஈ) `['chennai', 'mylapore']`  
      `['mumbai', 'andheri']`  

8. Dictionary தரவுகளை குறிக்க இவற்றுள் எது ஒரு பொருளை உருவாக்குகின்றது?
   அ) listreader()
   ஆ) reader()
   இ) tuplereader()
   ஈ) DictReader()

9. ஏற்கனவே உள்ள கோப்பில் உள்ள தரவுகளில் சில மாற்றங்கள் செய்வதும் அல்லது மேலும் தரவை சேர்ப்பதும் எவ்வாறு அழைக்கலாம்?
   அ) பதிப்பித்தல்
   ஆ) இறுதியில் சேர்த்தல் (Appending)
   இ) மாற்றம் செய்தல்
   ஈ) திருத்துதல்

10. `test.csv` என்ற கோப்பில் பின்வரும் நிரல் என்ன விவரத்தை எழுதும்?
    ```python
    import csv
    D = [['Exam'],['Quarterly'],['Halfyearly']]
    csv.register_dialect('M',lineterminator = '\n')
    with open('c:\\pyprg\\ch13\\line2.csv', 'w') as f:
        wr = csv.writer(f,dialect='M')
        wr.writerows(D)
    f.close()
    ```
    அ) Exam Quarterly Halfyearly  
    ஆ) Exam Quarterly Halfyearly  
    இ) E  
       Q  
       H  
    ஈ) Exam  
       Quarterly  
       Halfyearly  

---

### பகுதி - ஆ: அனைத்து வினாக்களுக்கும் விடையளி (2 மதிப்பெண்)

1. CSV கோப்பு என்றால் என்ன?
2. பைத்தான் மூலம் CSV கோப்பை படிப்பதற்கான இரு வழிகளை குறிப்பிடுக.
3. கோப்பின் கொடாநிலை முறைமைகளை குறிப்பிடுக.
4. `next()` செயற்கூறின் பயன்பாடு என்ன?
5. CSV கோப்பில் ஒன்றுக்கு மேற்பட்ட நெடுவரிசையை எவ்வாறு வரிசையாக்கம் செய்வாய்? எடுத்துக்காட்டுத் தருக.

---

### பகுதி - இ: அனைத்து வினாக்களுக்கும் விடையளி (3 மதிப்பெண்)

1. பைத்தானிலுள்ள `open()` செயற்கூற்றை பற்றி குறிப்பு எழுதுக. மேலும் இதன் இரண்டு வழிமுறைகளின் வேறுபாடுகள் என்ன?
2. ஏற்கனவே உள்ள கோப்பில் மாற்றம் செய்யும் பைத்தான் நிரலை எழுதுக.
3. காற்புள்ளியை (,) தானமைவு பிரிப்பானாக கொண்டுள்ள CSV கோப்பினை படிப்பதற்கான பைத்தான் நிரலை எழுதுக.
4. write மற்றும் append முறைமைகளின் வேறுபாடு என்ன?
5. `reader()` மற்றும் `DictReader()` இடையேயான வேறுபாடு யாது?

---

### பகுதி - ஈ: அனைத்து வினாக்களுக்கும் விடையளி (5 மதிப்பெண்)

1. எக்ஸெல் மற்றும் CSV கோப்பின் வேறுபாடு என்ன?
2. பல்வேறு கோப்பு முறைமைகளின் பொருள்களைப் பட்டியலிடுக.
3. பைத்தானில் ஒரு கோப்பை படிப்பதற்கான பல்வேறு வழிமுறைகளை எழுதுக.
4. தனிப்பயனான மேற்கோள் பிரிப்பானுடன் கூடிய CSV கோப்பை எழுதுவதற்கான பைத்தான் நிரலை எழுதுக.
5. CSV கோப்பிலுள்ள தரவை வடிவமைப்பதற்கு பின்பற்றவேண்டிய விதிமுறைகளை எழுதுக.
