# College Management System - Database Design Documentation

## 1. Introduction

The Database Design Document defines the structure, relationships, and organization of data used by the College Management System (CMS).

The database is designed to store and manage academic, administrative, financial, and communication-related information securely.

The database follows a relational database model to maintain data consistency, reduce redundancy, and support efficient data retrieval.

---

# 2. Database Technology Selection

## Selected Database

**PostgreSQL**

## Reason for Selection

PostgreSQL is selected because:

- Supports complex relational data structures.
- Provides strong data integrity.
- Supports advanced SQL queries.
- Handles large amounts of data.
- Provides security features.
- Supports cloud deployment.
- Compatible with Django framework.

---

# 3. Database Design Principles

The database design follows:

## Normalization

The database will follow normalization principles to:

- Reduce duplicate data.
- Improve data consistency.
- Maintain data integrity.

## Data Integrity

The system will maintain:

- Primary key constraints.
- Foreign key relationships.
- Unique constraints.
- Validation rules.

---

# 4. Main Database Entities

The College Management System contains the following major entities:

| No | Entity | Description |
|----|--------|-------------|
| 1 | User | Stores all system users |
| 2 | Role | Stores user permissions |
| 3 | Student | Stores student information |
| 4 | Parent | Stores parent details |
| 5 | Faculty | Stores faculty information |
| 6 | Department | Stores departments |
| 7 | Course | Stores course details |
| 8 | Subject | Stores subject information |
| 9 | Attendance | Stores attendance records |
| 10 | Examination | Stores exam details |
| 11 | Result | Stores student results |
| 12 | Fee | Stores fee information |
| 13 | Payment | Stores payment transactions |
| 14 | Scholarship | Stores scholarship details |
| 15 | Book | Stores library books |
| 16 | Library Transaction | Stores book issue/return records |
| 17 | Hostel | Stores hostel information |
| 18 | Transport | Stores transport details |
| 19 | Company | Stores placement companies |
| 20 | Notification | Stores system notifications |

---

# 5. Entity Relationship Overview

                Role
                  |
                  |
                User
                  |
   --------------------------------
   |              |               |
   ↓              ↓               ↓

Student Faculty Admin

   |
   |
   ↓

Department
|
|
↓

Course
   |
   |
   ↓

Subject


---

# 6. Database Tables Design

---

# 6.1 User Table

## Purpose

Stores authentication information for all users.

## Table Name

`users`

## Columns

| Column | Data Type | Description |
|--------|-----------|-------------|
| id | Integer | Primary key |
| username | VARCHAR | Username |
| email | VARCHAR | User email |
| password_hash | VARCHAR | Encrypted password |
| role_id | Integer | Foreign key |
| phone | VARCHAR | Contact number |
| status | Boolean | Account status |
| created_at | Timestamp | Account creation date |

---

# 6.2 Role Table

## Table Name

`roles`

## Columns

| Column | Data Type | Description |
|--------|-----------|-------------|
| id | Integer | Primary key |
| role_name | VARCHAR | Role name |

Examples:

- Super Admin
- Student
- Faculty
- Accountant

---

# 6.3 Student Table

## Table Name

`students`

## Columns

| Column | Data Type | Description |
|--------|-----------|-------------|
| id | Integer | Primary key |
| user_id | Integer | Foreign key |
| admission_number | VARCHAR | Student ID |
| first_name | VARCHAR | First name |
| last_name | VARCHAR | Last name |
| date_of_birth | DATE | DOB |
| gender | VARCHAR | Gender |
| department_id | Integer | Foreign key |
| course_id | Integer | Foreign key |
| admission_date | DATE | Admission date |

---

# 6.4 Parent Table

## Table Name

`parents`

## Columns

| Column | Data Type | Description |
|--------|-----------|-------------|
| id | Integer | Primary key |
| student_id | Integer | Foreign key |
| name | VARCHAR | Parent name |
| phone | VARCHAR | Contact number |
| email | VARCHAR | Email |

---

# 6.5 Faculty Table

## Table Name

`faculty`

## Columns

| Column | Data Type | Description |
|--------|-----------|-------------|
| id | Integer | Primary key |
| user_id | Integer | Foreign key |
| faculty_name | VARCHAR | Name |
| department_id | Integer | Department |
| qualification | VARCHAR | Qualification |
| joining_date | DATE | Joining date |

---

# 6.6 Department Table

## Table Name

`departments`

## Columns

| Column | Data Type | Description |
|--------|-----------|-------------|
| id | Integer | Primary key |
| department_name | VARCHAR | Name |
| department_code | VARCHAR | Code |

---

# 6.7 Course Table

## Table Name

`courses`

## Columns

| Column | Data Type | Description |
|--------|-----------|-------------|
| id | Integer | Primary key |
| department_id | Integer | Foreign key |
| course_name | VARCHAR | Course name |
| duration | Integer | Years |

---

# 6.8 Subject Table

## Table Name

`subjects`

## Columns

| Column | Data Type | Description |
|--------|-----------|-------------|
| id | Integer | Primary key |
| course_id | Integer | Foreign key |
| subject_name | VARCHAR | Subject name |
| credits | Integer | Credit value |

---

# 6.9 Attendance Table

## Table Name

`attendance`

## Columns

| Column | Data Type | Description |
|--------|-----------|-------------|
| id | Integer | Primary key |
| student_id | Integer | Student |
| subject_id | Integer | Subject |
| date | DATE | Attendance date |
| status | VARCHAR | Present/Absent |

---

# 6.10 Examination Table

## Table Name

`examinations`

## Columns

| Column | Data Type | Description |
|--------|-----------|-------------|
| id | Integer | Primary key |
| exam_name | VARCHAR | Exam name |
| course_id | Integer | Course |
| exam_date | DATE | Date |

---

# 6.11 Result Table

## Table Name

`results`

## Columns

| Column | Data Type | Description |
|--------|-----------|-------------|
| id | Integer | Primary key |
| student_id | Integer | Student |
| subject_id | Integer | Subject |
| marks | Integer | Marks |
| grade | VARCHAR | Grade |

---

# 6.12 Fee Table

## Table Name

`fees`

## Columns

| Column | Data Type | Description |
|--------|-----------|-------------|
| id | Integer | Primary key |
| student_id | Integer | Student |
| amount | Decimal | Fee amount |
| due_date | DATE | Payment deadline |
| status | VARCHAR | Paid/Pending |

---

# 6.13 Library Book Table

## Table Name

`books`

## Columns

| Column | Data Type | Description |
|--------|-----------|-------------|
| id | Integer | Primary key |
| title | VARCHAR | Book title |
| author | VARCHAR | Author |
| isbn | VARCHAR | ISBN number |
| quantity | Integer | Available copies |

---

# 7. Entity Relationships

## User and Role

Relationship:


Role 1 --------- Many Users


One role can have multiple users.

---

## Department and Course

Relationship:


Department 1 -------- Many Courses


One department contains multiple courses.

---

## Course and Subject

Relationship:


Course 1 -------- Many Subjects


One course contains multiple subjects.

---

## Student and Attendance

Relationship:


Student 1 -------- Many Attendance Records


A student can have multiple attendance records.

---

## Student and Results

Relationship:


Student 1 -------- Many Results


A student can have multiple results.

---

# 8. Database Security

Security measures:

- Password encryption.
- Role-based database access.
- Data validation.
- Regular backups.
- Restricted database permissions.

---

# 9. Backup Strategy

The system will implement:

- Daily database backups.
- Backup restoration testing.
- Secure backup storage.
- Disaster recovery procedures.

---

# 10. Future Database Enhancements

Future improvements:

- Multi-college database support.
- Data warehouse integration.
- Advanced analytics database.
- AI model data storage.

---

# 11. Conclusion

The database design provides a structured foundation for the College Management System.

The relational database model ensures secure storage, efficient data management, and scalability for future system expansion.