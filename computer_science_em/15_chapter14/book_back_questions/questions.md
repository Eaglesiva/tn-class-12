# Standard 12 Computer Science - Chapter 14: Importing C++ Programs in Python
## Book-Back Evaluation Questions (Questions Only)

> **Textbook Printed Pages:** 274 – 277  
> **Source HTML Links:**
> - [Page 274 HTML](file:///e:/19.03.26/new%20project/tn_school_books/12th/computer_science_em/full_book/05_integrating_python_mysql_cpp/01_importing_cpp_programs/page_274/page_274.html)
> - [Page 275 HTML](file:///e:/19.03.26/new%20project/tn_school_books/12th/computer_science_em/full_book/05_integrating_python_mysql_cpp/01_importing_cpp_programs/page_275/page_275.html)
> - [Page 276 HTML](file:///e:/19.03.26/new%20project/tn_school_books/12th/computer_science_em/full_book/05_integrating_python_mysql_cpp/01_importing_cpp_programs/page_276/page_276.html)
> - [Page 277 HTML](file:///e:/19.03.26/new%20project/tn_school_books/12th/computer_science_em/full_book/05_integrating_python_mysql_cpp/01_importing_cpp_programs/page_277/page_277.html)

---

### Hands on Experience

1. Write a C++ program to create a class called Student with the following details:  
   **Protected member:**  
   - `Rno` integer  
   **Public members:**  
   - `void Readno(int);` to accept roll number and assign to Rno  
   - `void Writeno();` To display Rno.  

   The class Test is derived Publically from the Student class contains the following details:  
   **Protected member:**  
   - `Mark1` float  
   - `Mark2` float  
   **Public members:**  
   - `void Readmark(float, float);` To accept mark1 and mark2  
   - `void Writemark();` To display the marks  

   Create a class called Sports with the following detail:  
   **Protected members:**  
   - `score` integer  
   **Public members:**  
   - `void Readscore(int);` To accept the score  
   - `void Writescore();` To display the score  

   The class Result is derived Publically from Test and Sports class contains the following details:  
   **Private member:**  
   - `Total` float  
   **Public member:**  
   - `void display()` assign the sum of mark1, mark2, score in total. Invoke `Writeno()`, `Writemark()` and `Writescore()`. Display the total also.  

   Save the C++ program in a file called hybrid. Write a python program to execute the `hybrid.cpp`.

2. Write a C++ program to print boundary elements of a matrix and name the file as `Border.cpp`. Write a python program to execute the `Border.cpp`.

---

### Part - I: Choose the best answer (1 Mark)

1. Which of the following is not a scripting language?
   a) JavaScript
   b) PHP
   c) Perl
   d) HTML

2. Importing C++ program in a Python program is called
   a) wrapping
   b) Downloading
   c) Interconnecting
   d) Parsing

3. The expansion of API is
   a) Application Programming Interpreter
   b) Application Programming Interface
   c) Application Performing Interface
   d) Application Programming Interlink

4. A framework for interfacing Python and C++ is
   a) Ctypes
   b) SWIG
   c) Cython
   d) Boost

5. Which of the following is a software design technique to split your code into separate parts?
   a) Object oriented Programming
   b) Modular programming
   c) Low Level Programming
   d) Procedure oriented Programming

6. The module which allows you to interface with the Windows operating system is
   a) OS module
   b) sys module
   c) csv module
   d) getopt module

7. `getopt()` will return an empty array if there is no error in splitting strings to
   a) argv variable
   b) opt variable
   c) args variable
   d) ifile variable

8. Identify the function call statement in the following snippet:
   ```python
   if __name__ =='__main__':
       main(sys.argv[1:])
   ```
   a) main(sys.argv[1:])
   b) `__name__`
   c) `__main__`
   d) argv

9. Which of the following can be used for processing text, numbers, images, and scientific data?
   a) HTML
   b) C
   c) C++
   d) PYTHON

10. What does `__name__` contains ?
    a) c++ filename
    b) main() name
    c) python filename
    d) os module name

---

### Part - II: Answer the following questions (2 Marks)

1. What is the theoretical difference between Scripting language and other programming language?
2. Differentiate compiler and interpreter.
3. Write the expansion of:
   (i) SWIG  
   (ii) MinGW  
4. What is the use of modules?
5. What is the use of cd command. Give an example.

---

### Part - III: Answer the following questions (3 Marks)

1. Differentiate PYTHON and C++.
2. What are the applications of scripting language?
3. What is MinGW? What is its use?
4. Identify the module, operator, definition name for the following:
   `welcome.display()`
5. What is `sys.argv`? What does it contain?

---

### Part - IV: Answer the following questions (5 Marks)

1. Write any 5 features of Python.
2. Explain each word of the following command:
   `Python <filename.py> -<i> <C++ filename without cpp extension>`
3. What is the purpose of sys, os, getopt module in Python. Explain.
4. Write the syntax for `getopt()` and explain its arguments and return values.
5. Write a Python program to execute the following C++ coding:
   ```cpp
   #include <iostream>
   using namespace std;
   int main()
   {
       cout << "WELCOME";
       return(0);
   }
   ```
   The above C++ program is saved in a file `welcome.cpp`.
