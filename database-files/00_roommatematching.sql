DROP DATABASE IF EXISTS roommates;
CREATE DATABASE IF NOT EXISTS roommates;
USE roommates;

CREATE TABLE dormBuilding (
    dormId INT,
    numRooms INT,
    occupancy INT,
    maxCapacity INT,
    bedsAvailable INT,
    address VARCHAR(200),
    amenities VARCHAR(200),
    name VARCHAR(100),
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
