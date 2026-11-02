# Standard 12 Computer Science - Chapter 16: Data Visualization using Pyplot
## Book-Back Evaluation Questions (Questions Only)

> **Textbook Printed Pages:** 316 – 320  
> **Source HTML Links:**
> - [Page 316 HTML](file:///e:/19.03.26/new%20project/tn_school_books/12th/computer_science_em/full_book/05_integrating_python_mysql_cpp/03_data_visualization_pyplot/page_316/page_316.html)
> - [Page 317 HTML](file:///e:/19.03.26/new%20project/tn_school_books/12th/computer_science_em/full_book/05_integrating_python_mysql_cpp/03_data_visualization_pyplot/page_317/page_317.html)
> - [Page 318 HTML](file:///e:/19.03.26/new%20project/tn_school_books/12th/computer_science_em/full_book/05_integrating_python_mysql_cpp/03_data_visualization_pyplot/page_318/page_318.html)
> - [Page 319 HTML](file:///e:/19.03.26/new%20project/tn_school_books/12th/computer_science_em/full_book/05_integrating_python_mysql_cpp/03_data_visualization_pyplot/page_319/page_319.html)
> - [Page 320 HTML](file:///e:/19.03.26/new%20project/tn_school_books/12th/computer_science_em/full_book/05_integrating_python_mysql_cpp/03_data_visualization_pyplot/page_320/page_320.html)

---

### Hands on Practice

1. Plot a line chart for the given data and set the title for x and y axis:  
   **Average Pulse:** 80, 85, 90, 95, 100  
   **Calorie Burnage:** 240, 250, 260, 270, 280  
2. Plot a pie chart for your marks in the recent examination.
3. Plot a line chart on the academic performance of Class 12 students in Computer Science for the past 10 years.
4. Plot a bar chart for the number of computer science periods in a week.

---

### Part - I: Choose the best answer (1 Mark)

1. Which is a python package used for 2D charts?
   a) matplotlib.pyplot
   b) matplotlib.pip
   c) matplotlib.numpy
   d) matplotlib.plt

2. Identify the package manager for installing Python packages, or modules.
   a) Matplotlib
   b) PIP
   c) plt.show()
   d) python package

3. Which of the following feature is used to represent data and information graphically?
   a) Data List
   b) Data Tuple
   c) Classes and Objects
   d) Data Visualization

4. .......... is a collection of resources assembled to create a single unified visual display.
   a) Interface
   b) Dashboard
   c) Objects
   d) Graphics

5. Which of the following module should be imported to visualize data and information in Python?
   a) csv
   b) getopt
   c) mysql
   d) matplotlib

6. ............ is a type of chart which displays information as a series of data points connected by straight line segments.
   a) csv
   b) Pie chart
   c) Bar chart
   d) All the above

7. Read the code:
   ```python
   import matplotlib.pyplot as plt
   plt.plot(3,2)
   plt.show()
   ```
   Identify the output for the above coding:  
   a) A bar chart with X axis and Y axis showing multiple bars  
   b) A line chart with title 'Epic Info'  
   c) A plot showing a single point at coordinates (3, 2)  
   d) A linear continuous line graph passing through origin  

8. Identify the right type of chart using the following hints:  
   **Hint 1:** This chart is often used to visualize a trend in data over intervals of time.  
   **Hint 2:** The line in this type of chart is often drawn chronologically.  
   a) Line chart
   b) Bar chart
   c) Pie chart
   d) Scatter plot

9. Read the statements given below. Identify the right option from the following for pie chart:  
   **Statement A:** To make a pie chart with Matplotlib, we can use the `plt.pie()` function.  
   **Statement B:** The `autopct` parameter allows us to display the percentage value using the Python string formatting.  
   a) Statement A is correct
   b) Statement B is correct
   c) Both the statements are correct
   d) Both the statements are wrong

---

### Part - II: Answer the following questions (2 Marks)

1. What is Data Visualization?
2. List the general types of data visualization.
3. List the types of Visualizations in Matplotlib.
4. How will you install Matplotlib?
5. Write the difference between the following functions:
   - `plt.plot([1,2,3,4])`
   - `plt.plot([1,2,3,4], [1,4,9,16])`

---

### Part - III: Answer the following questions (3 Marks)

1. Draw the output for the following data visualization plot:
   ```python
   import matplotlib.pyplot as plt
   plt.bar([1,3,5,7,9],[5,2,7,8,2], label="Example one")
   plt.bar([2,4,6,8,10],[8,6,2,5,6], label="Example two", color='g')
   plt.legend()
   plt.xlabel('bar number')
   plt.ylabel('bar height')
   plt.title('Epic Graph\nAnother Line! Whoa')
   plt.show()
   ```
2. Write any three uses of data visualization.
3. Write the plot for the following pie chart output.

---

### Part - IV: Answer the following questions (5 Marks)

1. Explain in detail the types of pyplots using Matplotlib.
2. Explain the various buttons in a matplotlib window.
3. Explain the purpose of the following functions:
   a) `plt.xlabel`  
   b) `plt.ylabel`  
   c) `plt.title`  
   d) `plt.legend()`  
   e) `plt.show()`  
