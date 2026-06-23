# Cloud-Based Data Redundancy Removal System (DRRS)

## Overview

The **Cloud-Based Data Redundancy Removal System (DRRS)** is a web application developed to prevent duplicate data from being stored in a cloud database. The system validates user data before insertion and ensures that only unique and verified records are stored, improving database accuracy, integrity, and efficiency.

## Problem Statement

Duplicate records in databases increase storage usage, reduce data quality, and negatively impact application performance. This project implements a validation mechanism that detects duplicate records before insertion and prevents redundant data from entering the database.

## Features

* User-friendly web interface
* Data validation before insertion
* Duplicate email detection
* Prevents redundant records from being stored
* Stores only unique and verified data
* Microsoft SQL Server (MSSQL) database integration
* Simple and scalable Flask backend

## Technologies Used

* Python
* Flask
* HTML
* CSS
* Microsoft SQL Server (MSSQL)
* Pyodbc
* Git & GitHub

## Project Structure

```text
DRRS/
│
├── app.py
├── requirements.txt
├── database/
│   └── database.sql
├── templates/
│   ├── index.html
│   └── result.html
└── README.md
```

## Workflow

1. User enters record details.
2. Flask receives the submitted data.
3. The system validates the input.
4. The database checks whether the email already exists.
5. If a duplicate is found, the record is rejected.
6. If the record is unique, it is stored in the database.
7. The system displays the appropriate success or duplicate message.

## Future Enhancements

* Duplicate detection using multiple fields
* Admin dashboard
* Search and filter records
* Record update and delete functionality
* Cloud deployment
* User authentication and authorization
* Reporting and analytics dashboard
