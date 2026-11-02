# Standard 12 Computer Science - Chapter 3: Scoping
## Book-Back Evaluation Questions (Questions Only)

> **Textbook Printed Pages:** 28 – 30  
> **Source HTML Links:**
> - [Page 28 HTML](file:///e:/19.03.26/new%20project/tn_school_books/12th/computer_science_em/full_book/01_problem_solving_techniques/03_scoping/page_28/page_28.html)
> - [Page 29 HTML](file:///e:/19.03.26/new%20project/tn_school_books/12th/computer_science_em/full_book/01_problem_solving_techniques/03_scoping/page_29/page_29.html)
> - [Page 30 HTML](file:///e:/19.03.26/new%20project/tn_school_books/12th/computer_science_em/full_book/01_problem_solving_techniques/03_scoping/page_30/page_30.html)

---

### Hands on Practice

1. Observe the following diagram and Write the pseudo code for the following:
   ```
   sum( )
       num1:=10
       sum1( )
           num1: = num1 + 10
           sum2( )
               num1:=20
               num1:=num1 + 10
           sum2( )
       sum1( )
       print num1
   sum( )
   ```

---

### Part - I: Choose the best answer (1 Mark)

1. Which of the following refers to the visibility of variablesin one part of a program to another part of the same program.
   a) Scope
   b) Memory
   c) Address
   d) Accessibility

2. The process of binding a variable name with an object is called
   a) Scope
   b) Mapping
   c) late binding
   d) early binding

3. Which of the following is used in programming languages to map the variable and object?
   a) ::
   b) :=
   c) =
   d) ==

4. Containers for mapping names of variables to objects is called
   a) Scope
   b) Mapping
   c) Binding
   d) Namespaces

5. Which scope refers to variables defined in current function?
   a) Local Scope
   b) Global scope
   c) Module scope
   d) Function Scope

6. The process of subdividing a computer program into separate sub-programs is called
   a) Procedural Programming
   b) Modular programming
   c) Event Driven Programming
   d) Object oriented Programming

7. Which of the following security technique that regulates who canuse resources in a computing environment?
   a) Password
   b) Authentication
   c) Access control
   d) Certification

8. Which of the following members of a class can be handled only from within the class?
   a) Public members
   b) Protected members
   c) Secured members
   d) Private members

9. Which members are accessible from outside the class?
   a) Public members
   b) Protected members
   c) Secured members
   d) Private members

10. The members that are accessible from within the class and are also available to its sub-classes is called
   a) Public members
   b) Protected members
   c) Secured members
   d) Private members

---

### Part - II: Answer the following questions (2 Marks)

1. What is a scope?
2. Why scope should be used for variable. State the reason.
3. What is Mapping?
4. What do you mean by Namespaces?
5. How Python represents the private and protected Access specifiers?

---

### Part - III: Answer the following questions (3 Marks)

1. Define Local scope with an example.
2. Define Global scope with an example.
3. Define Enclosed scope with an example.
4. Why access control is required?
5. Identify the scope of the variables in the following pseudo code and write its output
   ```
   color:= 'Red'
   mycolor():
       b:='Blue'
       myfavcolor():
           g:='Green'
           print color, b, g
       myfavcolor()
       print color, b
   mycolor()
   print color
   ```

---

### Part - IV: Answer the following questions (5 Marks)

1. Explain the types of scopes for variable or LEGB rule with example.
2. Write any Five Characteristics of Modules.
3. Write any five benefits in using modular programming.
