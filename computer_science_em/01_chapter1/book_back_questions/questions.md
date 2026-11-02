# Standard 12 Computer Science - Chapter 1: Function
## Book-Back Evaluation Questions (Questions Only)

> **Textbook Printed Pages:** 8 – 10  
> **Source HTML Links:**
> - [Page 8 HTML](file:///e:/19.03.26/new%20project/tn_school_books/12th/computer_science_em/full_book/01_problem_solving_techniques/01_function/page_8/page_8.html)
> - [Page 9 HTML](file:///e:/19.03.26/new%20project/tn_school_books/12th/computer_science_em/full_book/01_problem_solving_techniques/01_function/page_9/page_9.html)
> - [Page 10 HTML](file:///e:/19.03.26/new%20project/tn_school_books/12th/computer_science_em/full_book/01_problem_solving_techniques/01_function/page_10/page_10.html)

---

### Part - I: Choose the best answer (1 Mark)

1. The small sections of code that are used to perform a particular task is called
   a) Subroutines
   b) Files
   c) Pseudo code
   d) Modules

2. Which of the following is a unit of code that is often defined within a greater code structure?
   a) Subroutines
   b) Function
   c) Files
   d) Modules

3. Which of the following is a distinct syntactic block?
   a) Subroutines
   b) Function
   c) Definition
   d) Modules

4. The variables in a function definition are called as
   a) Subroutines
   b) Function
   c) Definition
   d) Parameters

5. The values which are passed to a function definition are called
   a) Arguments
   b) Subroutines
   c) Function
   d) Definition

6. Which of the following are mandatory to write the type annotations in the function definition?
   a) { }
   b) ( )
   c) [ ]
   d) < >

7. Which of the following defines what an object can do?
   a) Operating System
   b) Compiler
   c) Interface
   d) Interpreter

8. Which of the following carries out the instructions defined in the interface?
   a) Operating System
   b) Compiler
   c) Implementation
   d) Interpreter

9. The functions which will give exact result when same arguments are passed are called
   a) Impure functions
   b) Partial Functions
   c) Dynamic Functions
   d) Pure functions

10. The functions which cause side effects to the arguments passed are called
   a) impure function
   b) Partial Functions
   c) Dynamic Functions
   d) Pure functions

---

### Hands on Practice

1. Write algorithmic function definition to find the minimum among 3 numbers.
2. Write algorithmic recursive function definition to find the sum of n natural numbers.

---

### Part - II: Answer the following questions (2 Marks)

1. What is a subroutine?
2. Define Function with respect to Programming language.
3. Write the inference you get from `X:=(78)`.
4. Differentiate interface and implementation.
5. Which of the following is a normal function definition and which is recursive function definition
   i)
   ```
   let sum x y:
       return x + y
   ```
   ii)
   ```
   let disp :
       print 'welcome'
   ```
   iii)
   ```
   let rec sum num:
       if (num!=0) then return num + sum (num-1)
       else
           return num
   ```

---

### Part - III: Answer the following questions (3 Marks)

1. Mention the characteristics of Interface.
2. Why strlen is called pure function?
3. What is the side effect of impure function. Give example.
4. Differentiate pure and impure function.

---

### Part - IV: Answer the following questions (5 Marks)

1. What are called Parameters and write a note on
   (i) Parameter without Type
   (ii) Parameter with Type

2. Identify in the following program
   ```
   let rec gcd a b :=
       if b <> 0 then gcd b (a mod b) else return a
   ```
   i) Name of the function  
   ii) Identify the statement which tells it is a recursive function  
   iii) Name of the argument variable  
   iv) Statement which invoke the function recursively  
   v) Statement which terminates the recursion  

3. Explain with example Pure and impure functions.

4. Explain with an example interface and implementation.
