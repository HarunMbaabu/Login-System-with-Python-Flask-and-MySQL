## Login System with Python Flask and MySQL for Beginners

### Requirements(Minimum)

Download and install Python, I am using Python 3.7.2, make sure to check the box Add Python to PATH on the installation setup screen. </p>
Download and install MySQL Community Server and MySQL Workbench, you can skip this step if you already have a MySQL server set up. </p>


**Mojor operations handled**

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
          
### 1 .Create an environment
          
Depending on your operating system,make a virtual environment to avoid messing with your machine's primary dependencies
          
**Windows**
          
```

cd Login-System-with-Python-Flask-and-MySQL
py -3 -m venv venv

```
          
**macOS/Linux**
          
```
cd Login-System-with-Python-Flask-and-MySQL
python3 -m venv venv

```

### 2 .Activate the environment
          
**Windows** 

```venv\Scripts\activate```
          
**macOS/Linux**

```. venv/bin/activate```
or
```source venv/bin/activate```

### 3 .Install the requirements

Applies for windows/macOS/Linux

```pip install -r requirements.txt```
  
### 4. Run the application 

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
          

![Image description](https://github.com/HarunHM/Login-System-with-Python-Flask-and-MySQL/blob/master/static/Screenshot%20from%202020-01-11%2020-25-25.png?raw=true)
Note:-The version of python i use will change in future , so check your python IDE with latest version and if this doesn't work get in touch with me on twitter, https://twitter.com/HarunMbaabu.
