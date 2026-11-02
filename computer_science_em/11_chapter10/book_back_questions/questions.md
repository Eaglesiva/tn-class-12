# Standard 12 Computer Science - Chapter 10: Python Classes and Objects
## Book-Back Evaluation Questions (Questions Only)

> **Textbook Printed Pages:** 179 – 181  
> **Source HTML Links:**
> - [Page 179 HTML](file:///e:/19.03.26/new%20project/tn_school_books/12th/computer_science_em/full_book/03_modularity_and_oops/02_python_classes_objects/page_179/page_179.html)
> - [Page 180 HTML](file:///e:/19.03.26/new%20project/tn_school_books/12th/computer_science_em/full_book/03_modularity_and_oops/02_python_classes_objects/page_180/page_180.html)
> - [Page 181 HTML](file:///e:/19.03.26/new%20project/tn_school_books/12th/computer_science_em/full_book/03_modularity_and_oops/02_python_classes_objects/page_181/page_181.html)

---

### Hands on Experience

1. Write a program using class to store name and marks of students in list and print total marks.
2. Write a program using class to accept three sides of a triangle and print its area.
3. Write a menu driven program to read, display, add and subtract two distances.

---

### Part - I: Choose the best answer (1 Mark)

1. Which of the following are the key features of an Object Oriented Programming language?
   a) Constructor and Classes
   b) Constructor and Object
   c) Classes and Objects
   d) Constructor and Destructor

2. Functions defined inside a class:
   a) Functions
   b) Module
   c) Methods
   d) section

3. Class members are accessed through which operator?
   a) &
   b) .
   c) #
   d) %

4. Which of the following method is automatically executed when an object is created?
   a) `__object__( )`
   b) `__del__( )`
   c) `__func__( )`
   d) `__init__( )`

5. A private class variable is prefixed with
   a) `__`
   b) `&&`
   c) `##`
   d) `**`

6. Which of the following method is used as destructor?
   a) `__init__( )`
   b) `__dest__( )`
   c) `__rem__( )`
   d) `__del__( )`

7. Which of the following class declaration is correct?
   a) class class_name
   b) class class_name<>
   c) class class_name:
   d) class class_name[ ]

8. Which of the following is the output of the following program?
   ```python
   class Student:
       def __init__(self, name):
           self.name=name
           print (self.name)
   S=Student("Tamil")
   ```
   a) Error
   b) Tamil
   c) name
   d) self

9. Which of the following is the private class variable?
   a) `__num`
   b) `##num`
   c) `$$num`
   d) `&#`

10. The process of creating an object is called as:
    a) Constructor
    b) Destructor
    c) Initialize
    d) Instantiation

---

### Part - II: Answer the following questions (2 Marks)

1. What is class?
2. What is instantiation?
3. What is the output of the following program?
   ```python
   class Sample:
       __num=10
       def disp(self):
           print(self.__num)
   S=Sample()
   S.disp()
   print(S.__num)
   ```
4. How will you create constructor in Python?
5. What is the purpose of Destructor?

---

### Part - III: Answer the following questions (3 Marks)

1. What are class members? How do you define it?
2. Write a class with two private class variables and print the sum using a method.
3. Find the error in the following program to get the given output:
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
   **Output:**  
   Fruit 1 = Apple, Fruit 2 = Mango

4. What is the output of the following program?
   ```python
   class Greeting:
       def __init__(self, name):
           self.__name = name
       def display(self):
           print("Good Morning ", self.__name)
   obj=Greeting('Bindu Madhavan')
   obj.display()
   ```
5. How to define constructor and destructor in Python?

---

### Part - IV: Answer the following questions (5 Marks)

1. Explain about constructor and destructor with suitable example.
