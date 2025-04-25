# Connect DB and create tables if not exists
import os
from dotenv import load_dotenv, dotenv_values 
import mysql.connector
from mysql.connector import errorcode

load_dotenv()

config = {
  'user': os.getenv("DB_USER"),
  'password': os.getenv("DB_PASSWORD"),
  'host': os.getenv("DB_HOST"),
  'raise_on_warnings': True
}

DB_NAME = 'ems'

TABLES = {}
TABLES['employees'] = (
    "CREATE TABLE `employees` ("
    "  `employee_id` int NOT NULL AUTO_INCREMENT PRIMARY KEY,"
    "  `name` varchar(100) NOT NULL,"
    "  `date_of_birth` date NOT NULL,"
    "  `nid` int NOT NULL UNIQUE,"
    "  `email` varchar(255) NOT NULL UNIQUE,"
    "  `phone_no` varchar(255) NOT NULL UNIQUE,"
    "  `gender` enum('Male','Female', 'Other') NOT NULL,"
    "  `father_name` varchar(100) NOT NULL,"
    "  `mother_name` varchar(100) NOT NULL,"
    "  `marital_status` enum('Single', 'Married') NOT NULL,"
    "  `dept` varchar(100) NOT NULL,"
    "  `designation` varchar(100) NOT NULL,"
    "  `nationality` varchar(100) NOT NULL,"
    "  `joining_date` date NOT NULL,"
    "  `present_address` varchar(255) NOT NULL,"
    "  `permanent_address` varchar(255) NOT NULL"
    ") ENGINE=InnoDB")

TABLES['experiences'] = (
    "CREATE TABLE `experiences` ("
    "  `experience_id` int NOT NULL AUTO_INCREMENT PRIMARY KEY,"
    "  `employee_id` int NOT NULL,"
    "  `company_name` varchar(255) NOT NULL,"
    "  `position` varchar(255) NOT NULL,"
    "  `joining_date` date NOT NULL,"
    "  `ending_date` date NOT NULL,"
    "  `location` varchar(255) NOT NULL"
    ") ENGINE=InnoDB")

TABLES['degrees'] = (
    "CREATE TABLE `degrees` ("
    "  `degree_id` int NOT NULL AUTO_INCREMENT PRIMARY KEY,"
    "  `employee_id` int NOT NULL,"
    "  `degree_name` varchar(255) NOT NULL,"
    "  `institute_name` varchar(255) NOT NULL,"
    "  `major` varchar(255) NOT NULL,"
    "  `location` varchar(255) NOT NULL,"
    "  `gpa` float(3) NOT NULL,"
    "  `gpa_scale` float(3) NOT NULL,"
    "  `year_of_passing` year NOT NULL"
    ") ENGINE=InnoDB")

# Establish database connection
db_connection = mysql.connector.connect(**config)
cursor = db_connection.cursor()

# Create database
def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8mb4'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(DB_NAME))
        db_connection.database = DB_NAME
    else:
        print(err)
        exit(1)

for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

def get_db_connection():
    return mysql.connector.connect(**config)

cursor.close()
db_connection.close()