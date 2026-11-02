# Standard 12 Computer Science - Chapter 13: Python and CSV Files
## Book-Back Evaluation Questions (Questions Only)

> **Textbook Printed Pages:** 256 – 258  
> **Source HTML Links:**
> - [Page 256 HTML](file:///e:/19.03.26/new%20project/tn_school_books/12th/computer_science_em/full_book/04_database_concepts_and_mysql/03_python_csv_files/page_256/page_256.html)
> - [Page 257 HTML](file:///e:/19.03.26/new%20project/tn_school_books/12th/computer_science_em/full_book/04_database_concepts_and_mysql/03_python_csv_files/page_257/page_257.html)
> - [Page 258 HTML](file:///e:/19.03.26/new%20project/tn_school_books/12th/computer_science_em/full_book/04_database_concepts_and_mysql/03_python_csv_files/page_258/page_258.html)

---

### Hands on Experience

1. Write a Python program to read the following `Namelist.csv` file and sort the data in alphabetically order of names in a list and display the output:

   | SNO | NAME | OCCUPATION |
   | :--- | :--- | :--- |
   | 1 | NIVETHITHA | ENGINEER |
   | 2 | ADHITH | DOCTOR |
   | 3 | LAVANYA | SINGER |
   | 4 | VIDHYA | TEACHER |
   | 5 | BINDHU | LECTURER |

2. Write a Python program to accept the name and five subjects mark of 5 students. Find the total and store all the details of the students in a CSV file.

---

### Part - I: Choose the best answer (1 Mark)

1. A CSV file is also known as a ….
   a) Flat File
   b) 3D File
   c) String File
   d) Random File

2. The expansion of CRLF is
   a) Control Return and Line Feed
   b) Carriage Return and Form Feed
   c) Control Router and Line Feed
   d) Carriage Return and Line Feed

3. Which of the following module is provided by Python to do several operations on the CSV files?
   a) py
   b) xls
   c) csv
   d) os

4. Which of the following mode is used when dealing with non-text files like image or exe files?
   a) Text mode
   b) Binary mode
   c) xls mode
   d) csv mode

5. The command used to skip a row in a CSV file is
   a) next()
   b) skip()
   c) omit()
   d) bounce()

6. Which of the following is a string used to terminate lines produced by `writer()` method of csv module?
   a) Line Terminator
   b) Enter key
   c) Form feed
   d) Data Terminator

7. What is the output of the following program?
   ```python
   import csv
   d=csv.reader(open('c:\\PYPRG\\ch13\\city.csv'))
   next(d)
   for row in d:
       print(row)
   ```
   if the file called "city.csv" contain the following details:
   ```
   chennai,mylapore
   mumbai,andheri
   ```
   a) `['chennai', 'mylapore']`  
   b) `['mumbai', 'andheri']`  
   c) `['chennai']`  
   d) `['chennai', 'mylapore']`  
      `['mumbai', 'andheri']`  

8. Which of the following creates an object which maps data to a dictionary?
   a) listreader()
   b) reader()
   c) tuplereader()
   d) DictReader ()

9. Making some changes in the data of the existing file or adding more data is called
   a) Editing
   b) Appending
   c) Modification
   d) Alteration

10. What will be written inside the file test.csv using the following program:
    ```python
    import csv
    D = [['Exam'],['Quarterly'],['Halfyearly']]
    csv.register_dialect('M',lineterminator = '\n')
    with open('c:\\pyprg\\ch13\\line2.csv', 'w') as f:
        wr = csv.writer(f,dialect='M')
        wr.writerows(D)
    f.close()
    ```
    a) Exam Quarterly Halfyearly  
    b) Exam Quarterly Halfyearly  
    c) E  
       Q  
       H  
    d) Exam  
       Quarterly  
       Halfyearly  

---

### Part - II: Answer the following questions (2 Marks)

1. What is CSV File?
2. Mention the two ways to read a CSV file using Python.
3. Mention the default modes of the File.
4. What is use of next() function?
5. How will you sort more than one column from a csv file? Give an example statement.

---

### Part - III: Answer the following questions (3 Marks)

1. Write a note on open() function of python. What is the difference between the two methods?
2. Write a Python program to modify an existing file.
3. Write a Python program to read a CSV file with default delimiter comma (,).
4. What is the difference between the write mode and append mode.
5. What is the difference between reader() method and DictReader() class?

---

### Part - IV: Answer the following questions (5 Marks)

1. Differentiate Excel file and CSV file.
2. Tabulate the different mode with its meaning.
3. Write the different methods to read a File in Python.
4. Write a Python program to write a CSV File with custom quotes.
5. Write the rules to be followed to format the data in a CSV file.
