-- #
-- # Converted from MS Access 2010 Northwind database (northwind.accdb) using
-- # Bullzip MS Access to MySQL Version 5.1.242. http://www.bullzip.com
-- #
-- # CHANGES MADE AFTER INITIAL CONVERSION
-- # * column and row names in CamelCase converted to lower_case_with_underscore
-- # * space and slash ("/") in table and column names replaced with _underscore_
-- # * id column names converted to "id"
-- # * foreign key column names converted to xxx_id
-- # * variables of type TIMESTAMP converted to DATETIME to avoid TIMESTAMP
-- #   range limitation (1997 - 2038 UTC), and other limitations.
-- # * unique and foreign key checks disabled while loading data
-- #
-- #------------------------------------------------------------------
-- #

-- SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
-- SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;

-- USE `northwind`;


-- -- Dorms
-- INSERT INTO dormBuilding VALUES
--     (1, 100, 90, 100, 10, "", ""),
--     (2, 80, 75, 80, 5, "", "");

-- -- Students
-- INSERT INTO student VALUES
--     (1, 'Bob', 'Smith'),
--     (2, 'Alice', 'Johnson');

-- -- Student Emails
-- INSERT INTO student_email VALUES
--     (1, 'bob.smith@northeastern.edu'),
--     (2, 'alice.johnson@northeastern.edu');

-- -- Dorm Rooms
-- INSERT INTO dorm_room VALUES
--     (101, 1, 1),
--     (102, 2, 1);

-- -- Preferences
-- INSERT INTO preferences VALUES
--     (1, 22, 'Quiet at night', false),
--     (2, 2, 'Studies late', true);

-- -- Applications
-- INSERT INTO applications VALUES
--     (301, 1),
--     (302, 2);

-- -- RAs
-- INSERT INTO RA VALUES
--     (1, 'Renee', 'Williams');

-- -- Events
-- INSERT INTO events VALUES
--     ('2025-04-15 18:00:00', 'Pizza Night', 'Dorm A Lounge', 1),
--     ('2025-04-20 19:00:00', 'Study Jam', 'Library Room 3', 1);

-- -- Complaints
-- INSERT INTO complaints VALUES
--     (101, 1, 'Noise at midnight'),
--     (102, 2, 'Roommate smokes indoors');

-- -- Student-RA Bridge
-- INSERT INTO studentBridgeRA VALUES
--     (1, 1),
--     (2, 1);

-- -- RA-Event Bridge
-- INSERT INTO RABridgeEvents VALUES
--     (1, '2025-04-15 18:00:00', 'Pizza Night'),
--     (1, '2025-04-20 19:00:00', 'Study Jam');

-- -- RA-Complaint Bridge
-- INSERT INTO RABridgeComplaints VALUES
--     (1, 101),
--     (1, 102);


-- SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
-- SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;