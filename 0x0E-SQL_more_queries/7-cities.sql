-- lists all the tables of a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE PRIMARY KEY, name VARCHAR(256) NOT NULL);
