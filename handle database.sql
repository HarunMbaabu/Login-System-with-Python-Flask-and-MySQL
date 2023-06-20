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



