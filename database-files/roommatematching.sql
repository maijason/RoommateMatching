
DROP DATABASE IF EXISTS roommates;
CREATE DATABASE IF NOT EXISTS roommates;
USE roommates;

CREATE TABLE dormBuilding (
    dormId INT,
    numRooms INT,
    occupancy INT,
    maxCapacity INT,
    bedsAvailable INT,
    PRIMARY KEY (dormId)
);

CREATE TABLE student (
    stuId INT,
    firstName VARCHAR(20),
    lastName VARCHAR(20),
    PRIMARY KEY (stuId)
);

CREATE TABLE dorm_room (
    roomNum INT,
    stuId INT,
    dormId INT,
    PRIMARY KEY (roomNum, dormId),
    FOREIGN KEY (stuId) REFERENCES student(stuId) ON UPDATE RESTRICT ON DELETE RESTRICT,
    FOREIGN KEY (dormId) REFERENCES dormBuilding(dormId) ON UPDATE RESTRICT ON DELETE RESTRICT
);

CREATE TABLE student_email (
    stuId INT,
    email VARCHAR(50),
    PRIMARY KEY (stuId, email),
    FOREIGN KEY (stuId) REFERENCES student(stuId) ON UPDATE RESTRICT ON DELETE RESTRICT
);

CREATE TABLE preferences (
    stuId INT,
    sleepTime INT,
    extra_observations VARCHAR(100),
    smoking BOOLEAN,
    PRIMARY KEY (stuId),
    FOREIGN KEY (stuId) REFERENCES student(stuId) ON UPDATE RESTRICT ON DELETE RESTRICT
);

CREATE TABLE applications (
    appId INT,
    stuId INT,
    PRIMARY KEY (appId),
    FOREIGN KEY (stuId) REFERENCES student(stuId) ON UPDATE RESTRICT ON DELETE RESTRICT
);

CREATE TABLE RA (
    raId INT,
    firstName VARCHAR(20),
    lastName VARCHAR(20),
    PRIMARY KEY (raId)
);

CREATE TABLE events (
    datetime DATETIME,
    title VARCHAR(20),
    location VARCHAR(30),
    raId INT,
    PRIMARY KEY (datetime, title),
    FOREIGN KEY (raId) REFERENCES RA(raId) ON UPDATE RESTRICT ON DELETE RESTRICT
);

CREATE TABLE complaints (
    compId INT,
    stuId INT,
    description VARCHAR(150),
    PRIMARY KEY (compId),
    FOREIGN KEY (stuId) REFERENCES student(stuId) ON UPDATE RESTRICT ON DELETE RESTRICT
);

CREATE TABLE studentBridgeRA (
    stuId INT,
    raId INT,
    PRIMARY KEY (stuId, raId),
    FOREIGN KEY (stuId) REFERENCES student(stuId) ON UPDATE RESTRICT ON DELETE RESTRICT,
    FOREIGN KEY (raId) REFERENCES RA(raId) ON UPDATE RESTRICT ON DELETE RESTRICT
);

CREATE TABLE RABridgeEvents (
    raId INT,
    datetime DATETIME,
    title VARCHAR(20),
    PRIMARY KEY (raId, datetime, title),
    FOREIGN KEY (raId) REFERENCES RA(raId) ON UPDATE RESTRICT ON DELETE RESTRICT,
    FOREIGN KEY (datetime, title) REFERENCES events(datetime, title) ON UPDATE RESTRICT ON DELETE RESTRICT
);

CREATE TABLE RABridgeComplaints (
    raId INT,
    compId INT,
    PRIMARY KEY (raId, compId),
    FOREIGN KEY (raId) REFERENCES RA(raId) ON UPDATE RESTRICT ON DELETE RESTRICT,
    FOREIGN KEY (compId) REFERENCES complaints(compId) ON UPDATE RESTRICT ON DELETE RESTRICT
);

CREATE TABLE housingAdmin (
    haId INT,
    firstName VARCHAR(15),
    lastName VARCHAR(15),
    PRIMARY KEY (haId)
);

CREATE TABLE conflicts (
    confId INT,
    urgency BOOLEAN,
    housingAdminId INT,
    PRIMARY KEY (confId),
    FOREIGN KEY (housingAdminId) REFERENCES housingAdmin(haId) ON UPDATE RESTRICT ON DELETE RESTRICT
);

CREATE TABLE conflicts_student (
    confId INT,
    studentId INT,
    PRIMARY KEY (confId, studentId),
    FOREIGN KEY (confId) REFERENCES conflicts(confId) ON UPDATE RESTRICT ON DELETE RESTRICT,
    FOREIGN KEY (studentId) REFERENCES student(stuId) ON UPDATE RESTRICT ON DELETE RESTRICT
);

CREATE TABLE dormBuildingBridgeHousingAdmin (
    dormId INT,
    haId INT,
    PRIMARY KEY (dormId, haId),
    FOREIGN KEY (dormId) REFERENCES dormBuilding(dormId) ON UPDATE RESTRICT ON DELETE RESTRICT,
    FOREIGN KEY (haId) REFERENCES housingAdmin(haId) ON UPDATE RESTRICT ON DELETE RESTRICT
);

CREATE TABLE systemAdmin (
    adminId INT,
    firstName VARCHAR(20),
    lastName VARCHAR(20),
    PRIMARY KEY (adminId)
);

CREATE TABLE clearanceLevels (
    userId INT,
    role VARCHAR(30),
    clearance VARCHAR(30),
    PRIMARY KEY (userId)
);

CREATE TABLE systemAdminBridgeClearanceLevel (
    userId INT,
    adminId INT,
    PRIMARY KEY (userId, adminId),
    FOREIGN KEY (userId) REFERENCES clearanceLevels(userId) ON UPDATE RESTRICT ON DELETE RESTRICT,
    FOREIGN KEY (adminId) REFERENCES systemAdmin(adminId) ON UPDATE RESTRICT ON DELETE RESTRICT
);

CREATE TABLE systemAdminBridgeHousingAdmin (
    adminId INT,
    haId INT,
    PRIMARY KEY (adminId, haId),
    FOREIGN KEY (adminId) REFERENCES systemAdmin(adminId) ON UPDATE RESTRICT ON DELETE RESTRICT,
    FOREIGN KEY (haId) REFERENCES housingAdmin(haId) ON UPDATE RESTRICT ON DELETE RESTRICT
);

CREATE TABLE systemAdminBridgeConflicts (
    adminId INT,
    confId INT,
    PRIMARY KEY (adminId, confId),
    FOREIGN KEY (adminId) REFERENCES systemAdmin(adminId) ON UPDATE RESTRICT ON DELETE RESTRICT,
    FOREIGN KEY (confId) REFERENCES conflicts(confId) ON UPDATE RESTRICT ON DELETE RESTRICT
);

-- Dorms
INSERT INTO dormBuilding VALUES
    (1, 100, 90, 100, 10),
    (2, 80, 75, 80, 5);

-- Students
INSERT INTO student VALUES
    (1, 'Bob', 'Smith'),
    (2, 'Alice', 'Johnson');

-- Student Emails
INSERT INTO student_email VALUES
    (1, 'bob.smith@northeastern.edu'),
    (2, 'alice.johnson@northeastern.edu');

-- Dorm Rooms
INSERT INTO dorm_room VALUES
    (101, 1, 1),
    (102, 2, 1);

-- Preferences
INSERT INTO preferences VALUES
    (1, 22, 'Quiet at night', false),
    (2, 2, 'Studies late', true);

-- Applications
INSERT INTO applications VALUES
    (301, 1),
    (302, 2);

-- RAs
INSERT INTO RA VALUES
    (1, 'Renee', 'Williams');

-- Events
INSERT INTO events VALUES
    ('2025-04-15 18:00:00', 'Pizza Night', 'Dorm A Lounge', 1),
    ('2025-04-20 19:00:00', 'Study Jam', 'Library Room 3', 1);

-- Complaints
INSERT INTO complaints VALUES
    (101, 1, 'Noise at midnight'),
    (102, 2, 'Roommate smokes indoors');

-- Student-RA Bridge
INSERT INTO studentBridgeRA VALUES
    (1, 1),
    (2, 1);

-- RA-Event Bridge
INSERT INTO RABridgeEvents VALUES
    (1, '2025-04-15 18:00:00', 'Pizza Night'),
    (1, '2025-04-20 19:00:00', 'Study Jam');

-- RA-Complaint Bridge
INSERT INTO RABridgeComplaints VALUES
    (1, 101),
    (1, 102);

-- Housing Admins
INSERT INTO housingAdmin VALUES
    (1, 'Jane', 'Doe'),
    (2, 'Mark', 'Lee');

-- Conflicts
INSERT INTO conflicts VALUES
    (201, TRUE, 1),
    (202, FALSE, 2);

-- Conflict-Student Bridge
INSERT INTO conflicts_student VALUES
    (201, 1),
    (202, 2);

-- Dorm-HousingAdmin Bridge
INSERT INTO dormBuildingBridgeHousingAdmin VALUES
    (1, 1),
    (2, 2);

-- System Admins
INSERT INTO systemAdmin VALUES
    (1, 'Sam', 'Taylor'),
    (2, 'Alex', 'Smith');

-- Clearance Levels
INSERT INTO clearanceLevels VALUES
    (101, 'RA', 'medium'),
    (102, 'HA', 'high');

-- SystemAdmin-ClearanceLevel Bridge
INSERT INTO systemAdminBridgeClearanceLevel VALUES
    (101, 1),
    (102, 2);

-- SystemAdmin-HousingAdmin Bridge
INSERT INTO systemAdminBridgeHousingAdmin VALUES
    (1, 1),
    (2, 2);

-- SystemAdmin-Conflicts Bridge
INSERT INTO systemAdminBridgeConflicts VALUES
    (1, 201),
    (2, 202);

-- View dorm locations and availability (Bob)
SELECT dormId, numRooms, occupancy, maxCapacity, bedsAvailable FROM dormBuilding;

-- View detailed information about each dorm (Bob)
SELECT dormId, numRooms, occupancy, bedsAvailable FROM dormBuilding;

-- Access resident contact info for an RA (Renee)
SELECT s.stuId, s.firstName, s.lastName, e.email
FROM student s
JOIN student_email e ON s.stuId = e.stuId
JOIN studentBridgeRA sr ON s.stuId = sr.stuId
WHERE sr.raId = 1;

-- View anonymous complaints from students (Renee)
SELECT compId, description
FROM complaints
WHERE stuId IN (
  SELECT stuId FROM studentBridgeRA WHERE raId = 1
);

-- View overview of complaints and events (Renee)
SELECT c.compId, c.description, e.title, e.datetime
FROM complaints c
JOIN studentBridgeRA sr ON c.stuId = sr.stuId
LEFT JOIN RABridgeEvents re ON sr.raId = re.raId
LEFT JOIN events e ON re.datetime = e.datetime AND re.title = e.title
WHERE sr.raId = 1;

-- View all events for an RA in calendar order (Renee)
SELECT title, datetime, location FROM events WHERE raId = 1 ORDER BY datetime ASC;

-- Count of roommate conflicts per dorm (Jane)
SELECT db.dormId, COUNT(cs.confId) AS conflict_count
FROM dormBuilding db
JOIN dorm_room dr ON db.dormId = dr.dormId
JOIN conflicts_student cs ON cs.studentId = dr.stuId
JOIN conflicts c ON c.confId = cs.confId
GROUP BY db.dormId;

-- View roommate match success rates per dorm (Jane)
SELECT dormId, COUNT(*) AS successful_matches FROM dorm_room GROUP BY dormId;

-- Summary report of dorm building stats (Jane)
SELECT dormId, numRooms, occupancy, maxCapacity, bedsAvailable FROM dormBuilding;

-- View all users and their roles/clearance levels
SELECT userId, role, clearance
FROM clearanceLevels;

-- View system admins and the complaints they can access
SELECT sac.adminId, sa.firstName, sa.lastName, c.confId, c.urgency
FROM systemAdminBridgeConflicts sac
JOIN systemAdmin sa ON sac.adminId = sa.adminId
JOIN conflicts c ON sac.confId = c.confId;

-- View which system admins are managing which users (with clearance info)
SELECT sa.adminId, sa.firstName, sa.lastName, cl.userId, cl.role, cl.clearance
FROM systemAdmin sa
JOIN systemAdminBridgeClearanceLevel sbcl ON sa.adminId = sbcl.adminId
JOIN clearanceLevels cl ON sbcl.userId = cl.userId;