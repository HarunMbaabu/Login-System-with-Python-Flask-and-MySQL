## Login System with Python Flask and MySQL for Beginners

>>  **When you make contributions please test your code before sending a PR.** 

```python 
>>> python unit_test.py
```

### Requirements(Minimum)

Download and install Python, I am using Python 3.7.2, make sure to check the box Add Python to PATH on the installation setup screen. </p>
Download and install MySQL Community Server and MySQL Workbench, you can skip this step if you already have a MySQL server set up. </p>


**Major operations handled**

1). Form Design — Design a login and registration form with HTML5 and CSS3.<br>
2). Templates — Create Flask templates with HTML and Python.<br>
3). Basic Validation — Validating form data that is sent to the server (username, password, and email).<br>
4). Session Management — Initialize sessions and store retrieved database results.<br>
5). MySQL Queries — Select and insert records from/in our database table.<br>
6). Routes — Routing will allow us to point our URL's to our functions.<br>

### Requirements ,Packages used and Installation
Download and install Python, for this tutorial I'll be using Python 3.7.2, make sure to check the box Add Python to PATH on the installation setup screen
 
### Installation
Navigate to your current project directory for this case it will be **Login-System-with-Python-Flask-and-MySQL**. <br>

### 1 .Fork the repository and Clone it into your local machine
```csharp
git clone https://github.com/{your-Github-Username }/Login-System-with-Python-Flask-and-MySQL.git
```
          
### 2 .Create an environment
> Check to make sure you are in the same directory where you did the git clone,if not navigate to that specific directory.

Depending on your operating system,make a virtual environment to avoid messing with your machine's primary dependencies
          
**Windows**
          
```csharp
cd Login-System-with-Python-Flask-and-MySQL
py -3 -m venv venv

```
          
**macOS/Linux**
          
```csharp
cd Login-System-with-Python-Flask-and-MySQL
python3 -m venv venv

```

### 3 .Activate the environment
          
**Windows** 

```venv\Scripts\activate```
          
**macOS/Linux**

```. venv/bin/activate```
or
```source venv/bin/activate```

### 4 .Install the requirements

Applies for windows/macOS/Linux

```csharp
pip install -r requirements.txt
```


### 6. Create the database and table 

```sql
-- Create the  database named "loginapp"
CREATE DATABASE loginapp;


-- Switch to 'loginapp' database; 
USE loginapp; 


-- Create 'account' table with id, username,email, password columns. 
CREATE TABLE accounts (
  id INT PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL
); 
```

### 6. Run the application 

**For linux and macOS**
Make the run file executable by running the code

```chmod 777 run```

Then start the application by executing the run file

```./run```

**On windows**
```
set FLASK_APP=main
flask run

```
### Application Flow. 

**Register Page:**

![Image description](https://github.com/HarunMbaabu/Login-System-with-Python-Flask-and-MySQL/blob/master/static/images/Screenshot%20from%202023-09-17%2018-29-57.png?raw=true)  

**Log In Page:** 

![Image description](https://github.com/HarunMbaabu/Login-System-with-Python-Flask-and-MySQL/blob/master/static/images/Screenshot%20from%202023-09-17%2018-29-52.png?raw=true)

**Home Page After Log In:**

![Image description](https://github.com/HarunMbaabu/Login-System-with-Python-Flask-and-MySQL/blob/master/static/images/Screenshot%20from%202023-09-17%2018-29-28.png?raw=true)

Note:-The version of python i use will change in future , so check your python IDE with latest version and if this doesn't work get in touch with me on twitter, https://twitter.com/HarunMbaabu. 
