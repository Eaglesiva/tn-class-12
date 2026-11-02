# Standard 12 Computer Science (தமிழ் வழி) - அத்தியாயம் 10: பைத்தான் இனக்குழுக்கள் மற்றும் பொருள்கள்
## Book-Back Evaluation Questions (Questions Only)

> **பாடநூல் அச்சிடப்பட்ட பக்கங்கள்:** 183 – 186  
> **Source HTML Links:**
> - [பக்கம் 183 HTML](file:///e:/19.03.26/new%20project/tn_school_books/12th/computer_science_tm/full_book/03_koorunilai_porulnookku_niraalaakkam/02_python_inakuzhukkal_porulgal/page_183/page_183.html)
> - [பக்கம் 184 HTML](file:///e:/19.03.26/new%20project/tn_school_books/12th/computer_science_tm/full_book/03_koorunilai_porulnookku_niraalaakkam/02_python_inakuzhukkal_porulgal/page_184/page_184.html)
> - [பக்கம் 185 HTML](file:///e:/19.03.26/new%20project/tn_school_books/12th/computer_science_tm/full_book/03_koorunilai_porulnookku_niraalaakkam/02_python_inakuzhukkal_porulgal/page_185/page_185.html)
> - [பக்கம் 186 HTML](file:///e:/19.03.26/new%20project/tn_school_books/12th/computer_science_tm/full_book/03_koorunilai_porulnookku_niraalaakkam/02_python_inakuzhukkal_porulgal/page_186/page_186.html)

---

### செய்முறைப் பயிற்சி

1. இனக்குழுவைப் பயன்படுத்தி மாணவர்களின் பெயர் மற்றும் மதிப்பெண்களைப் பட்டியலாக சேமித்து மொத்த மதிப்பெண்ணை அச்சிடும் பைத்தான் நிரலை எழுதுக.
2. இனக்குழுவைப் பயன்படுத்தி முக்கோணத்தின் மூன்று பக்கங்களின் அளவை உள்ளீடாகப் பெற்று பரப்பளவைக் கண்டறியும் பைத்தான் நிரலை எழுதுக.
3. இரண்டு தூரங்களின் அளவை படிக்க, காண்பிக்க, கூட்ட மற்றும் கழிக்க உதவும் பட்டியல் முறை (Menu driven) நிரலை எழுதுக.

---

### பகுதி - அ: சரியான விடையைத் தேர்ந்தெடுத்து எழுதுக (1 மதிப்பெண்)

1. பின்வருவனவற்றுள் எவை பொருள் நோக்கு நிரலாக்கத்தின் முக்கிய அம்சம் ஆகும்?
   அ) ஆக்கி மற்றும் இனக்குழு
   ஆ) ஆக்கி மற்றும் பொருள்
   இ) இனக்குழு மற்றும் பொருள்
   ஈ) ஆக்கி மற்றும் அழிப்பி

2. இனக்குழுவின் உள்ளே வரையறுக்கப்படும் செயற்கூறு எது?
   அ) செயற்கூறு
   ஆ) கூறு
   இ) வழிமுறை
   ஈ) பிரிவு

3. இனக்குழு உறுப்புகள் எந்த செயற்குறியின் மூலம் அணுகப்படுகிறது?
   அ) &
   ஆ) .
   இ) #
   ஈ) %

4. பொருள் உருவாக்கப்படும் போது தானாகவே இயக்கப்படும் செயற்கூறு எது?
   அ) `__object__( )`
   ஆ) `__del__( )`
   இ) `__func__( )`
   ஈ) `__init__( )`

5. private இனக்குழு மாறியின் முன்னொட்டு எது?
   அ) `__`
   ஆ) `&&`
   இ) `##`
   ஈ) `**`

6. பின்வரும் வழிமுறைகளில் எது அழிப்பியாகப் பயன்படுகிறது?
   அ) `__init__( )`
   ஆ) `__dest__( )`
   இ) `__rem__( )`
   ஈ) `__del__( )`

7. பின்வருவனவற்றுள் எந்த இனக்குழு அறிவிப்பு சரியானது?
   அ) class class_name
   ஆ) class class_name<>
   இ) class class_name:
   ஈ) class class_name[ ]

8. பின்வரும் நிரலின் வெளியீடு என்ன?
   ```python
   class Student:
       def __init__(self, name):
           self.name=name
           print(self.name)
   S=Student("Tamil")
   ```
   அ) Error
   ஆ) Tamil
   இ) name
   ஈ) self

9. பின்வருவனவற்றுள் எது private இனக்குழு மாறி?
   அ) `__num`
   ஆ) `##num`
   இ) `$$num`
   ஈ) `&#`

10. பொருளை உருவாக்கும் செயல்முறை எது:
    அ) ஆக்கி
    ஆ) அழிப்பு
    இ) மதிப்பிருத்தல்
    ஈ) சான்றுருவாக்கல்

---

### பகுதி - ஆ: அனைத்து வினாக்களுக்கும் விடையளி (2 மதிப்பெண்)

1. இனக்குழு என்றால் என்ன?
2. சான்றுருவாக்கல் என்றால் என்ன?
3. பின்வரும் நிரலின் வெளியீடு என்ன?
   ```python
   class Sample:
       __num=10
       def disp(self):
           print(self.__num)
   S=Sample()
   S.disp()
   print(S.__num)
   ```
4. பைத்தானில் ஆக்கியை எவ்வாறு உருவாக்குவாய்?
5. அழிப்பியின் நோக்கம் என்ன?

---

### பகுதி - இ: அனைத்து வினாக்களுக்கும் விடையளி (3 மதிப்பெண்)

1. இனக்குழு உறுப்புகள் என்றால் என்ன? அதனை எவ்வாறு வரையறுப்பாய்?
2. இரண்டு private இனக்குழு மாறிகளுடன், வழிமுறையை பயன்படுத்தி கூட்டுத் தொகை sum அச்சிடும் இனக்குழுவை வரையறுக்கவும்.
3. கொடுக்கப்பட்ட வெளியீட்டை பெற பின்வரும் நிரலில் உள்ள பிழைகளை காண்க:
   ```python
   class Fruits:
       def __init__(self, f1, f2):
           self.f1=f1
           self.f2=f2
       def display(self):
           print("Fruit 1 = %s, Fruit 2 = %s" %(self.f1, self.f2))
   F = Fruits ('Apple', 'Mango')
   del F.display
   F.display()
   ```
   **வெளியீடு:**  
   Fruit 1 = Apple, Fruit 2 = Mango

4. பின்வரும் நிரலின் வெளியீடு என்ன?
   ```python
   class Greeting:
       def __init__(self, name):
           self.__name = name
       def display(self):
           print("Good Morning ", self.__name)
   obj=Greeting('Bindu Madhavan')
   obj.display()
   ```
5. பைத்தானில் ஆக்கி மற்றும் அழிப்பிகளை எவ்வாறு வரையறுப்பாய்?

---

### பகுதி - ஈ: அனைத்து வினாக்களுக்கும் விடையளி (5 மதிப்பெண்)

1. ஆக்கி மற்றும் அழிப்பி பற்றி பொருத்தமான எடுத்துக்காட்டுடன் விளக்குக.
