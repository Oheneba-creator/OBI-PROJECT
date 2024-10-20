CREATE DATaBASE schooldb;
USE  schooldb;

CREATE TABLE Students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    dob DATE,
    address TEXT,
    phone_number VARCHAR(20)
);

CREATE TABLE Teachers (
    teacher_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(50),
    email VARCHAR(100)
);

CREATE TABLE Courses (
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    course_name VARCHAR(100),
    teacher_id INT,
    FOREIGN KEY (teacher_id) REFERENCES Teachers(teacher_id)
);

CREATE TABLE Enrollments (
    enrollment_id INT PRIMARY   
 KEY AUTO_INCREMENT,
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN   
 KEY (course_id) REFERENCES Courses(course_id)
);

CREATE TABLE Grades   
 (
    grade_id INT PRIMARY KEY AUTO_INCREMENT,
    enrollment_id INT,
    grade DECIMAL(5,2),
    FOREIGN KEY (enrollment_id) REFERENCES Enrollments(enrollment_id)
);

  INSERT INTO Students (first_name, last_name, dob, address, phone_number)
VALUES
    ('Alice', 'Wonderland', '2000-01-01', '123 Wonderland Lane', '123-456-7890'),
    ('Bob', 'Builder', '1999-02-02', '456 Builder Street', '987-654-3210');

INSERT INTO Teachers (first_name, last_name, department, email)
VALUES
    ('Carol', 'Teacher', 'Science', 'carol@example.com'),
    ('David', 'Professor', 'Math', 'david@example.com');

INSERT INTO Courses (course_name, teacher_id)
VALUES
    ('Science 101', 1),
    ('Math 101', 2);

INSERT INTO Enrollments (student_id, course_id, enrollment_date)
VALUES
    (1, 1, '2023-09-01'),
    (1, 2, '2023-09-01'),
    (2, 1, '2023-09-01');

INSERT INTO Grades (enrollment_id, grade)
VALUES
    (1, 95),
    (2, 85),
    (3, 90);

-- List all students enrolled in Science 101
SELECT Students.first_name, Students.last_name
FROM Students
JOIN Enrollments ON Students.student_id = Enrollments.student_id
JOIN Courses ON Enrollments.course_id = Courses.course_id
WHERE Courses.course_name   
 = 'Science 101';

-- Find the average grade for Math 101
SELECT AVG(Grades.grade) AS average_grade
FROM Grades
JOIN Enrollments ON Grades.enrollment_id = Enrollments.enrollment_id
JOIN Courses ON Enrollments.course_id = Courses.course_id
WHERE Courses.course_name = 'Math 101';