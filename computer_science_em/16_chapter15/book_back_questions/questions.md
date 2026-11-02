# Standard 12 Computer Science - Chapter 15: Data Manipulation Through SQL
## Book-Back Evaluation Questions (Questions Only)

> **Textbook Printed Pages:** 303 – 306  
> **Source HTML Links:**
> - [Page 303 HTML](file:///e:/19.03.26/new%20project/tn_school_books/12th/computer_science_em/full_book/05_integrating_python_mysql_cpp/02_data_manipulation_sql/page_303/page_303.html)
> - [Page 304 HTML](file:///e:/19.03.26/new%20project/tn_school_books/12th/computer_science_em/full_book/05_integrating_python_mysql_cpp/02_data_manipulation_sql/page_304/page_304.html)
> - [Page 305 HTML](file:///e:/19.03.26/new%20project/tn_school_books/12th/computer_science_em/full_book/05_integrating_python_mysql_cpp/02_data_manipulation_sql/page_305/page_305.html)
> - [Page 306 HTML](file:///e:/19.03.26/new%20project/tn_school_books/12th/computer_science_em/full_book/05_integrating_python_mysql_cpp/02_data_manipulation_sql/page_306/page_306.html)

---

### Hands on Experience

1. Create an interactive program to accept the details from user and store it in a csv file using Python for the following table:  
   **Database name:** DB1  
   **Table name:** Customer  

   | Cust_Id | Cust_Name | Address | Phone_no | City |
   | :--- | :--- | :--- | :--- | :--- |
   | C008 | Sandeep | 14/1 Pritam Pura | 41206819 | Delhi |
   | C010 | Anurag Basu | 15A, Park Road | 61281921 | Kolkata |
   | C012 | Hrithik | 7/2 Vasant Nagar | 26121949 | Delhi |

2. Consider the following table GAMES. Write a python program to display the records for question (i) to (v):  
   **Table: GAMES**

   | Gcode | Name | GameName | Number | PrizeMoney | ScheduleDate |
   | :--- | :--- | :--- | :--- | :--- | :--- |
   | 101 | Padmaja | Carom Board | 2 | 5000 | 01-23-2014 |
   | 102 | Vidhya | Badminton | 2 | 12000 | 12-12-2013 |
   | 103 | Guru | Table Tennis | 4 | 8000 | 02-14-2014 |
   | 105 | Keerthana | Carom Board | 2 | 9000 | 01-01-2014 |
   | 108 | Krishna | Table Tennis | 4 | 25000 | 03-19-2014 |

   (i) To display the name of all Games with their Gcodes in descending order of their schedule date.  
   (ii) To display details of those games which are having Prize Money more than 7000.  
   (iii) To display the name and gamename of the Players in the ascending order of Gamename.  
   (iv) To display sum of PrizeMoney for each of the Number of participation groupings (as shown in column Number 4).  
   (v) Display all the records based on GameName.  

---

### Part - I: Choose the best answer (1 Mark)

1. Which of the following is an organized collection of data?
   a) Database
   b) DBMS
   c) Information
   d) Records

2. SQLite falls under which database system?
   a) Flat file database system
   b) Relational Database system
   c) Hierarchical database system
   d) Object oriented Database system

3. Which of the following is a control structure used to traverse and fetch the records of the database?
   a) Pointer
   b) Key
   c) Cursor
   d) Insertion point

4. Any changes made in the values of the record should be saved by the command
   a) Save
   b) Save As
   c) Commit
   d) Oblige

5. Which of the following executes the SQL command to perform some action?
   a) execute()
   b) key()
   c) cursor()
   d) run()

6. Which of the following function retrieves the average of a selected column of rows in a table?
   a) Add()
   b) SUM()
   c) AVG()
   d) AVERAGE()

7. The function that returns the largest value of the selected column is
   a) MAX()
   b) LARGE()
   c) HIGH()
   d) MAXIMUM()

8. Which of the following is called the master table?
   a) sqlite_master
   b) sql_master
   c) main_master
   d) master_main

9. The most commonly used statement in SQL is
   a) cursor
   b) select
   c) execute
   d) commit

10. Which of the following keyword avoid the duplicate?
    a) Distinct
    b) Remove
    c) Where
    d) GroupBy

---

### Part - II: Answer the following questions (2 Marks)

1. Mention the users who uses the Database.
2. Which method is used to connect a database? Give an example.
3. What is the advantage of declaring a column as "INTEGER PRIMARY KEY"?
4. Write the command to populate record in a table. Give an example.
5. Which method is used to fetch all rows from the database table?

---

### Part - III: Answer the following questions (3 Marks)

1. What is SQLite? What is its advantage?
2. Mention the difference between `fetchone()` and `fetchmany()`.
3. What is the use of Where Clause. Give a python statement using the where clause.
4. Read the following details. Based on that write a python script to display department wise records:  
   - **Database name:** `organization.db`  
   - **Table name:** `Employee`  
   - **Columns in the table:** `Eno`, `EmpName`, `Esal`, `Dept`  
5. Read the following details. Based on that write a python script to display records in descending order of `Eno`:  
   - **Database name:** `organization.db`  
   - **Table name:** `Employee`  
   - **Columns in the table:** `Eno`, `EmpName`, `Esal`, `Dept`  

---

### Part - IV: Answer the following questions (5 Marks)

1. Write in brief about SQLite and the steps used to use it.
2. Write the Python script to display all the records of the following table using `fetchmany()`:

   | Icode | ItemName | Rate |
   | :--- | :--- | :--- |
   | 1003 | Scanner | 10500 |
   | 1004 | Speaker | 3000 |
   | 1005 | Printer | 8000 |
   | 1008 | Monitor | 15000 |
   | 1010 | Mouse | 700 |

3. What is the use of HAVING clause. Give an example python script.
4. Write a Python script to create a table called ITEM with following specification. Add one record to the table:  
   - **Name of the database:** ABC  
   - **Name of the table:** Item  
   - **Column name and specification:**  
     - `Icode`: integer and act as primary key  
     - `Item Name`: Character with length 25  
     - `Rate`: Integer  
   - **Record to be added:** `1008, Monitor, 15000`  
5. Consider the following table Supplier and item. Write a python script for (i) to (ii):  
   **SUPPLIER**

   | Suppno | Name | City | Icode | SuppQty |
   | :--- | :--- | :--- | :--- | :--- |
   | S001 | Prasad | Delhi | 1008 | 100 |
   | S002 | Anu | Bangalore | 1010 | 200 |
   | S003 | Shahid | Bangalore | 1008 | 175 |
   | S004 | Akila | Hyderabad | 1005 | 195 |
   | S005 | Girish | Hyderabad | 1003 | 25 |
   | S006 | Shylaja | Chennai | 1008 | 180 |
   | S007 | Lavanya | Mumbai | 1005 | 325 |

   (i) Display Name, City and Itemname of suppliers who do not reside in Delhi.  
   (ii) Increment the SuppQty of Akila by 40.
