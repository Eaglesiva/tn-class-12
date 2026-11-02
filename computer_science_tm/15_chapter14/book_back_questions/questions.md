# Standard 12 Computer Science (தமிழ் வழி) - அத்தியாயம் 14: C++ நிரல்களைப் பைத்தானில் தருவித்தல்
## Book-Back Evaluation Questions (Questions Only)

> **பாடநூல் அச்சிடப்பட்ட பக்கங்கள்:** 281 – 284  
> **Source HTML Links:**
> - [பக்கம் 281 HTML](file:///e:/19.03.26/new%20project/tn_school_books/12th/computer_science_tm/full_book/05_python_mysql_c_orunginaithal/01_python_c_niralgal_tharuvithal/page_281/page_281.html)
> - [பக்கம் 282 HTML](file:///e:/19.03.26/new%20project/tn_school_books/12th/computer_science_tm/full_book/05_python_mysql_c_orunginaithal/01_python_c_niralgal_tharuvithal/page_282/page_282.html)
> - [பக்கம் 283 HTML](file:///e:/19.03.26/new%20project/tn_school_books/12th/computer_science_tm/full_book/05_python_mysql_c_orunginaithal/01_python_c_niralgal_tharuvithal/page_283/page_283.html)
> - [பக்கம் 284 HTML](file:///e:/19.03.26/new%20project/tn_school_books/12th/computer_science_tm/full_book/05_python_mysql_c_orunginaithal/01_python_c_niralgal_tharuvithal/page_284/page_284.html)

---

### செய்முறைப் பயிற்சி

1. கீழ்க்காணும் வரையறுப்புகளைக் கொண்ட Student என்னும் இனக்குழுவை உருவாக்கும் C++ நிரலை எழுதுக:  
   **Protected உறுப்புகள்:**  
   - `Rno` integer  
   **Public உறுப்புகள்:**  
   - `void Readno(int);` To accept roll number and assign to Rno  
   - `void Writeno();` To display Rno.  

   Student இனக்குழுவிலிருந்து public அணுகியல்புடன் தருவிக்கப்பட்ட Test என்னும் இனக்குழு கீழ்க்காணும் வரையறுப்புகளை கொண்டுள்ளது:  
   **Protected உறுப்புகள்:**  
   - `Mark1` float  
   - `Mark2` float  
   **Public உறுப்புகள்:**  
   - `void Readmark(float, float);` To accept mark1 and mark2  
   - `void Writemark();` To display the marks  

   கீழ்க்காணும் விவரங்களுடன் Sports என்ற இனக்குழுவை உருவாக்கவும்:  
   **Protected உறுப்புகள்:**  
   - `score` integer  
   **Public உறுப்புகள்:**  
   - `void Readscore(int);` To accept the score  
   - `void Writescore();` To display the score  

   Test மற்றும் Sports இனக்குழுக்களிலிருந்து public அணுகியல்புடன் தருவிக்கப்பட்ட Result என்னும் இனக்குழு கீழ்க்காணும் வரையறுப்புகளை கொண்டுள்ளது:  
   **Private உறுப்புகள்:**  
   - `Total` float  
   **Public உறுப்புகள்:**  
   - `void display()` assign the sum of mark1, mark2, score in total. Invoke `Writeno()`, `Writemark()` and `Writescore()`. Total-ஐ திரையில் காட்டும்.  

   C++ நிரலினை hybrid என்ற பெயரில் சேமிக்கவும். `hybrid.cpp` என்ற கோப்பை செயல்படுத்த ஒரு பைத்தான் நிரலை எழுதவும்.

2. ஒரு அணியின் (matrix) ஓர உறுப்புகளை (boundary elements) அச்சிடும் C++ நிரலை எழுதி, `Border.cpp` என்ற பெயரில் சேமித்து அதனை இயக்கும் பைத்தான் நிரல் ஒன்றை எழுதுக.

---

### பகுதி - அ: சரியான விடையைத் தேர்ந்தெடுத்து எழுதுக (1 மதிப்பெண்)

1. பின்வருவனவற்றுள் எது Scripting மொழி அல்ல?
   அ) ஜாவாஸ்கிரிப்ட்
   ஆ) PHP
   இ) பெர்ல்
   ஈ) HTML

2. பைத்தான் நிரலில் C++ நிரலை தருவித்தல் எவ்வாறு அழைக்கப்படுகிறது?
   அ) wrapping செய்தல்
   ஆ) பதிவிறக்கம் செய்தல்
   இ) இணைத்தல்
   ஈ) பிரித்தல்

3. API-ன் விரிவாக்கம்:
   அ) Application Programming Interpreter
   ஆ) Application Programming Interface
   இ) Application Performing Interface
   ஈ) Application Programming Interlink

4. பைத்தான் மற்றும் C++ நிரல்களை இடைமுகப்படுத்துவதற்கான கட்டமைப்பு:
   அ) Ctypes
   ஆ) SWIG
   இ) Cython
   ஈ) Boost

5. பின்வருவனவற்றுள் எது உங்கள் குறிமுறையை தனித்தனி பகுதிகளாக பிரித்தெடுப்பதற்கான மென்பொருள் வடிவமைப்பு தொழில்நுட்பம்?
   அ) பொருள்நோக்கு நிரலாக்கம்
   ஆ) கூறுநிலை நிரலாக்கம்
   இ) குறைந்த நிலை மொழி நிரலாக்கம்
   ஈ) செயல்முறை நோக்கு நிரலாக்கம்

6. நீங்கள் விண்டோஸ் இயக்க முறைமையுடன் தொடர்பு கொள்ள எந்த கூறுநிலை அனுமதிக்கிறது?
   அ) OS கூறுநிலை
   ஆ) sys கூறுநிலை
   இ) csv கூறுநிலை
   ஈ) getopt கூறுநிலை

7. சரங்களை எந்த மாதிரியாக பிரிக்கும்பொழுது பிழையின்றி அமைந்தால், `getopt()` வெற்று அணியை திருப்பி அனுப்பும்?
   அ) argv மாறி
   ஆ) opt மாறி
   இ) args மாறி
   ஈ) ifile மாறி

8. பின்வரும் நிரல் பகுதியில் உள்ள செயற்கூறின் அழைப்பு கூற்றை அடையாளம் காண்க:
   ```python
   if __name__ =='__main__':
       main(sys.argv[1:])
   ```
   அ) main(sys.argv[1:])
   ஆ) `__name__`
   இ) `__main__`
   ஈ) argv

9. கீழ்க்கண்டவற்றுள் எது உரை, எண்கள், படங்கள் மற்றும் அறிவியல் சார்ந்த தரவுகளை செயலாக்கப் பயன்படும்?
   அ) HTML
   ஆ) C
   இ) C++
   ஈ) PYTHON

10. `__name__` இது எதனைக் கொண்டுள்ளது ?
    அ) C++ கோப்புப் பெயர்
    ஆ) main() பெயர்
    இ) பைத்தான் கோப்புப் பெயர்
    ஈ) OS கூறுநிலைப் பெயர்

---

### பகுதி - ஆ: அனைத்து வினாக்களுக்கும் விடையளி (2 மதிப்பெண்)

1. Scripting மொழிக்கும், மற்ற நிரலாக்க மொழிக்கும் உள்ள தத்துவார்த்த வேறுபாடு யாது?
2. தொகுப்பான் மற்றும் வரிமொழி மாற்றியை வேறுபடுத்துக.
3. விரிவாக்கம் தருக:
   (i) SWIG  
   (ii) MinGW  
4. கூறுநிலைகளின் பயன் யாது?
5. cd கட்டளையின் பயன் யாது? எடுத்துக்காட்டு தருக.

---

### பகுதி - இ: அனைத்து வினாக்களுக்கும் விடையளி (3 மதிப்பெண்)

1. பைத்தான் மற்றும் C++ வேறுபடுத்துக.
2. Scripting மொழியின் பயன்பாடுகள் யாவை?
3. MinGW என்றால் என்ன? அதன் பயன் யாது?
4. கீழ்க்காணும் கூற்றில் கூறுநிலை, செயற்குறி, வரையறையின் பெயர் ஆகியவற்றை அடையாளம் காண்க:
   `welcome.display()`
5. sys.argv என்றால் என்ன? அது எதனைக் கொண்டுள்ளது?

---

### பகுதி - ஈ: அனைத்து வினாக்களுக்கும் விடையளி (5 மதிப்பெண்)

1. பைத்தானின் ஏதேனும் 5 சிறப்பம்சங்களை விவரிக்கவும்.
2. பின்வரும் கட்டளையின் ஒவ்வொரு பகுதியையும் விளக்கவும்:
   `Python <filename.py> -<i> <C++ filename without cpp extension>`
3. பைத்தானில் sys, os, getopt கூறுநிலைகளின் தேவை என்ன என்பதை விளக்குக.
4. `getopt()` என்ற செயற்கூறின் தொடரியலை எழுதி, அதன் செயலுருபுகளையும், திருப்பியனுப்பும் மதிப்புகளையும் விளக்குக.
5. கீழ்க்காணும் C++ நிரலை செயல்படுத்த ஒரு பைத்தான் நிரலை எழுதவும்:
   ```cpp
   #include <iostream>
   using namespace std;
   int main()
   {
       cout << "WELCOME";
       return(0);
   }
   ```
   மேலே கொடுக்கப்பட்டுள்ள C++ நிரல் `welcome.cpp` என்ற கோப்பில் சேமிக்கப்பட்டுள்ளது.
