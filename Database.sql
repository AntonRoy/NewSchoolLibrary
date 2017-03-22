CREATE DATABASE TSL
COLLATE Cyrillic_General_CI_AS
GO

CREATE TABLE Main_Tab
(
ID int NOT NULL IDENTITY,
ID_Vk int NULL,
ID_Card int NULL,
First_Name nvarchar(50) NULL,
Last_Name nvarchar(50) NULL,
Date_Of_Birth date NULL,
)
GO

CREATE TABLE Main_Books_Tab
(
ID int NOT NULL IDENTITY,
In_Stock int NULL,
All_Books int NULL,
Name_Of_Book nvarchar(150) NULL,
Author_Of_Book nvarchar(150) NULL,
)
GO

CREATE TABLE Book_Tab
(
ID int NOT NULL IDENTITY,
Type_Of_Book int NULL,
ID_Book nvarchar(150)
)

CREATE TABLE Books_Of_Student
(
ID int NOT NULL IDENTITY,
Student int NULL,
Book int NULL,
Date_Of_Receipt date NULL,
Date_Of_Return date NULL
)
GO

ALTER TABLE Main_Tab
ADD
PRIMARY KEY(ID)
GO

ALTER TABLE Book_Tab
ADD
PRIMARY KEY(ID)
GO

ALTER TABLE Main_Books_Tab
ADD
PRIMARY KEY(ID)
GO

ALTER TABLE Book_Tab
ADD
UNIQUE(Type_Of_Book)
GO

ALTER TABLE Book_Tab
ADD
FOREIGN KEY(Type_Of_Book) REFERENCES Main_Books_Tab(ID)
ON UPDATE CASCADE
GO

ALTER TABLE Books_Of_Student
ADD
UNIQUE(Student)
GO

ALTER TABLE Books_Of_Student
ADD
UNIQUE(Book)
GO

ALTER TABLE Books_Of_Student
ADD
FOREIGN KEY(Student) REFERENCES Main_Tab(ID)
ON UPDATE CASCADE
GO

ALTER TABLE Books_Of_Student
ADD
FOREIGN KEY(Book) REFERENCES Book_Tab(ID)
ON UPDATE CASCADE
GO

ALTER TABLE Books_Of_Student
ADD
CHECK (Date_Of_Receipt <= Date_Of_Return)
GO

ALTER TABLE Main_Books_Tab
ADD
CHECK ((In_Stock >= 0 and All_Books >= 0) and (In_Stock <= All_Books))
GO



