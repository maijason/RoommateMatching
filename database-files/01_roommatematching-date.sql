USE roommates;


-- Dorm Buildings (10 buildings) - Strong entity
INSERT INTO dormBuilding VALUES
    (1, 100, 90, 100, 10, '342 Huntington Ave', 'Gym, Study Rooms, Laundry', 'Speare Hall'),
    (2, 80, 75, 80, 5, '346 Huntington Ave', 'Study Rooms, Kitchen', 'White Hall'),
    (3, 200, 180, 200, 20, '10 Burke St', 'Game Room, Study Spaces, Music Room', 'International Village'),
    (4, 120, 110, 120, 10, '335 Huntington Ave', 'Gym, Laundry', 'Kennedy Hall'),
    (5, 90, 85, 90, 5, '151 Hemenway St', 'Study Spaces, Kitchen', 'East Village'),
    (6, 160, 140, 160, 20, '440 Huntington Ave', 'Laundry, Lounge', 'Smith Hall'),
    (7, 110, 100, 110, 10, '115 St. Stephen St', 'Kitchen, Study Room', 'West Village A'),
    (8, 150, 145, 150, 5, '117 St. Stephen St', 'Gym, Lounge', 'West Village B'),
    (9, 130, 120, 130, 10, '119 St. Stephen St', 'Study Spaces, Game Room', 'West Village C'),
    (10, 85, 80, 85, 5, '70 Leon St', 'Kitchen, Laundry', 'Davenport Commons');

-- Students (40 students) - Strong entity
INSERT INTO student VALUES
    (1, 'Bob', 'Smith'),
    (2, 'Alice', 'Johnson'),
    (3, 'Carlos', 'Rodriguez'),
    (4, 'Dina', 'Lee'),
    (5, 'Ethan', 'Brown'),
    (6, 'Fiona', 'Garcia'),
    (7, 'Gabriel', 'Martinez'),
    (8, 'Hannah', 'Nguyen'),
    (9, 'Ian', 'Wilson'),
    (10, 'Julia', 'Lopez'),
    (11, 'Kevin', 'Patel'),
    (12, 'Lana', 'Gonzalez'),
    (13, 'Miguel', 'Chen'),
    (14, 'Natalie', 'Kim'),
    (15, 'Oscar', 'Davis'),
    (16, 'Priya', 'Sharma'),
    (17, 'Quinn', 'Jackson'),
    (18, 'Ryan', 'Thompson'),
    (19, 'Sofia', 'Martin'),
    (20, 'Tyler', 'Wang'),
    (21, 'Uma', 'Harris'),
    (22, 'Victor', 'Taylor'),
    (23, 'Wendy', 'Clark'),
    (24, 'Xavier', 'Lewis'),
    (25, 'Yasmin', 'Allen'),
    (26, 'Zach', 'Young'),
    (27, 'Amelia', 'Walker'),
    (28, 'Ben', 'Hall'),
    (29, 'Chloe', 'Green'),
    (30, 'Daniel', 'Adams'),
    (31, 'Emma', 'Campbell'),
    (32, 'Felix', 'Mitchell'),
    (33, 'Grace', 'Roberts'),
    (34, 'Henry', 'Carter'),
    (35, 'Iris', 'Phillips'),
    (36, 'Jake', 'Evans'),
    (37, 'Kylie', 'Turner'),
    (38, 'Leo', 'Parker'),
    (39, 'Maya', 'Collins'),
    (40, 'Nate', 'Edwards');

-- Student Emails (40 emails)
INSERT INTO student_email VALUES
    (1, 'bob.smith@northeastern.edu'),
    (2, 'alice.johnson@northeastern.edu'),
    (3, 'c.rodriguez@northeastern.edu'),
    (4, 'd.lee@northeastern.edu'),
    (5, 'e.brown@northeastern.edu'),
    (6, 'f.garcia@northeastern.edu'),
    (7, 'g.martinez@northeastern.edu'),
    (8, 'h.nguyen@northeastern.edu'),
    (9, 'i.wilson@northeastern.edu'),
    (10, 'j.lopez@northeastern.edu'),
    (11, 'k.patel@northeastern.edu'),
    (12, 'l.gonzalez@northeastern.edu'),
    (13, 'm.chen@northeastern.edu'),
    (14, 'n.kim@northeastern.edu'),
    (15, 'o.davis@northeastern.edu'),
    (16, 'p.sharma@northeastern.edu'),
    (17, 'q.jackson@northeastern.edu'),
    (18, 'r.thompson@northeastern.edu'),
    (19, 's.martin@northeastern.edu'),
    (20, 't.wang@northeastern.edu'),
    (21, 'u.harris@northeastern.edu'),
    (22, 'v.taylor@northeastern.edu'),
    (23, 'w.clark@northeastern.edu'),
    (24, 'x.lewis@northeastern.edu'),
    (25, 'y.allen@northeastern.edu'),
    (26, 'z.young@northeastern.edu'),
    (27, 'a.walker@northeastern.edu'),
    (28, 'b.hall@northeastern.edu'),
    (29, 'c.green@northeastern.edu'),
    (30, 'd.adams@northeastern.edu'),
    (31, 'e.campbell@northeastern.edu'),
    (32, 'f.mitchell@northeastern.edu'),
    (33, 'g.roberts@northeastern.edu'),
    (34, 'h.carter@northeastern.edu'),
    (35, 'i.phillips@northeastern.edu'),
    (36, 'j.evans@northeastern.edu'),
    (37, 'k.turner@northeastern.edu'),
    (38, 'l.parker@northeastern.edu'),
    (39, 'm.collins@northeastern.edu'),
    (40, 'n.edwards@northeastern.edu');

-- Dorm Rooms (55 room assignments) - Weak entity
INSERT INTO dorm_room VALUES
    (101, 1, 1), (102, 2, 1), (103, 3, 1), (104, 4, 1), (105, 5, 1),
    (201, 6, 2), (202, 7, 2), (203, 8, 2), (204, 9, 2), (205, 10, 2),
    (301, 11, 3), (302, 12, 3), (303, 13, 3), (304, 14, 3), (305, 15, 3),
    (401, 16, 4), (402, 17, 4), (403, 18, 4), (404, 19, 4), (405, 20, 4),
    (501, 21, 5), (502, 22, 5), (503, 23, 5), (504, 24, 5), (505, 25, 5),
    (601, 26, 6), (602, 27, 6), (603, 28, 6), (604, 29, 6), (605, 30, 6),
    (701, 31, 7), (702, 32, 7), (703, 33, 7), (704, 34, 7), (705, 35, 7),
    (801, 36, 8), (802, 37, 8), (803, 38, 8), (804, 39, 8), (805, 40, 8),
    (106, NULL, 1), (107, NULL, 1), (206, NULL, 2), (306, NULL, 3), (307, NULL, 3),
    (406, NULL, 4), (506, NULL, 5), (606, NULL, 6), (607, NULL, 6), (706, NULL, 7),
    (806, NULL, 8), (807, NULL, 8), (308, NULL, 3), (408, NULL, 4), (508, NULL, 5);

-- Preferences (40 preference entries)
INSERT INTO preferences VALUES
    (1, 22, 'Quiet at night', false),
    (2, 23, 'Studies late', true),
    (3, 21, 'Early riser', false),
    (4, 24, 'Night owl', false),
    (5, 22, 'Likes music', false),
    (6, 23, 'Needs quiet for studying', true),
    (7, 21, 'Goes to gym in morning', false),
    (8, 22, 'Frequently has visitors', false),
    (9, 23, 'Light sleeper', true),
    (10, 24, 'Heavy sleeper', false),
    (11, 22, 'Vegetarian', false),
    (12, 23, 'Allergic to pets', true),
    (13, 21, 'Plays instruments', false),
    (14, 22, 'Neat and tidy', false),
    (15, 23, 'Minimalist', true),
    (16, 24, 'Has many plants', false),
    (17, 22, 'Gamer', false),
    (18, 23, 'Studious', true),
    (19, 21, 'Party-goer', false),
    (20, 22, 'Athlete', false),
    (21, 23, 'Sensitive to noise', true),
    (22, 24, 'Sensitive to light', false),
    (23, 22, 'Keeps irregular hours', false),
    (24, 23, 'Very social', true),
    (25, 21, 'Introverted', false),
    (26, 22, 'Art student', false),
    (27, 23, 'Engineering student', true),
    (28, 24, 'Business student', false),
    (29, 22, 'Film enthusiast', false),
    (30, 23, 'Book lover', true),
    (31, 21, 'Cooks often', false),
    (32, 22, 'Rarely cooks', false),
    (33, 23, 'Loves decorating', true),
    (34, 24, 'Minimalist style', false),
    (35, 22, 'Has service animal', false),
    (36, 23, 'Needs medical accommodations', true),
    (37, 21, 'Frequent video calls', false),
    (38, 22, 'Works part-time', false),
    (39, 23, 'Does volunteer work', true),
    (40, 24, 'Student government member', false);

-- Applications (40 applications)
INSERT INTO applications VALUES
    (301, 1), (302, 2), (303, 3), (304, 4), (305, 5),
    (306, 6), (307, 7), (308, 8), (309, 9), (310, 10),
    (311, 11), (312, 12), (313, 13), (314, 14), (315, 15),
    (316, 16), (317, 17), (318, 18), (319, 19), (320, 20),
    (321, 21), (322, 22), (323, 23), (324, 24), (325, 25),
    (326, 26), (327, 27), (328, 28), (329, 29), (330, 30),
    (331, 31), (332, 32), (333, 33), (334, 34), (335, 35),
    (336, 36), (337, 37), (338, 38), (339, 39), (340, 40);

-- RAs (30 RAs) - Strong entity
INSERT INTO RA VALUES
    (1, 'Renee', 'Williams'),
    (2, 'Marcus', 'Johnson'),
    (3, 'Sarah', 'Lee'),
    (4, 'Derek', 'Chen'),
    (5, 'Monica', 'Patel'),
    (6, 'Jacob', 'Garcia'),
    (7, 'Tiffany', 'Wilson'),
    (8, 'Andre', 'Thompson'),
    (9, 'Erica', 'Martinez'),
    (10, 'Brandon', 'Nguyen'),
    (11, 'Emily', 'Kim'),
    (12, 'Trevor', 'Brown'),
    (13, 'Leslie', 'Davis'),
    (14, 'Jamal', 'Taylor'),
    (15, 'Jennifer', 'Lopez'),
    (16, 'Chris', 'Walker'),
    (17, 'Aisha', 'Jackson'),
    (18, 'Daniel', 'Harris'),
    (19, 'Olivia', 'Clark'),
    (20, 'Michael', 'Rodriguez'),
    (21, 'Sophia', 'Martin'),
    (22, 'Jason', 'Allen'),
    (23, 'Rebecca', 'Wright'),
    (24, 'Nathan', 'Scott'),
    (25, 'Vanessa', 'Green'),
    (26, 'Keith', 'Baker'),
    (27, 'Alicia', 'Adams'),
    (28, 'David', 'Young'),
    (29, 'Maria', 'Hall'),
    (30, 'John', 'Evans');

-- Events (60 events) - Weak entity
INSERT INTO events VALUES
    ('2025-04-15 18:00:00', 'Pizza Night', 'Speare Hall Lounge', 1),
    ('2025-04-20 19:00:00', 'Study Jam', 'Library Room 3', 1),
    ('2025-04-18 17:30:00', 'Game Night', 'Smith Hall Lounge', 2),
    ('2025-04-22 16:00:00', 'Career Workshop', 'Career Center', 2),
    ('2025-04-17 19:30:00', 'Movie Night', 'IV Movie Room', 3),
    ('2025-04-24 18:30:00', 'Yoga Session', 'Marino Center', 3),
    ('2025-04-16 20:00:00', 'Karaoke Night', 'Kennedy Hall Lounge', 4),
    ('2025-04-23 17:00:00', 'Resume Review', 'Career Center', 4),
    ('2025-04-19 15:00:00', 'Campus Tour', 'Visitor Center', 5),
    ('2025-04-25 19:00:00', 'Talent Show', 'Blackman Auditorium', 5),
    ('2025-05-01 18:00:00', 'Cooking Class', 'Smith Hall Kitchen', 6),
    ('2025-05-03 14:00:00', 'Plant Workshop', 'Greenhouse', 6),
    ('2025-05-02 19:30:00', 'Open Mic Night', 'AfterHours', 7),
    ('2025-05-05 16:30:00', 'Study Break', 'WVA Lounge', 7),
    ('2025-05-04 18:00:00', 'Board Game Night', 'WVB Common Room', 8),
    ('2025-05-07 17:00:00', 'Stress Relief', 'WVC Lounge', 8),
    ('2025-05-06 19:00:00', 'Cultural Night', 'IV Common Room', 9),
    ('2025-05-09 18:30:00', 'Art Workshop', 'Art Studio', 9),
    ('2025-05-08 20:00:00', 'Trivia Night', 'Davenport Lounge', 10),
    ('2025-05-10 15:00:00', 'Sports Watch', 'Davenport TV Room', 10),
    ('2025-05-12 18:00:00', 'Ice Cream Social', 'Speare Hall Lobby', 11),
    ('2025-05-14 19:00:00', 'Meditation', 'Wellness Center', 11),
    ('2025-05-13 17:30:00', 'Job Fair Prep', 'Career Center', 12),
    ('2025-05-16 16:00:00', 'Community Service', 'Student Center', 12),
    ('2025-05-15 19:30:00', 'Film Screening', 'Snell Library', 13),
    ('2025-05-18 18:30:00', 'Poetry Reading', 'Afterhours', 13),
    ('2025-05-17 20:00:00', 'Dance Party', 'Smith Hall Lounge', 14),
    ('2025-05-20 17:00:00', 'Fitness Class', 'Marino Center', 14),
    ('2025-05-19 15:00:00', 'Study Group', 'Snell Library', 15),
    ('2025-05-22 19:00:00', 'Book Club', 'Reading Room', 15),
    ('2025-05-21 18:00:00', 'Bowling Night', 'Game Room', 16),
    ('2025-05-24 14:00:00', 'Hiking Trip', 'Meet at Visitor Center', 16),
    ('2025-05-23 19:30:00', 'Comedy Night', 'AfterHours', 17),
    ('2025-05-26 16:30:00', 'Craft Workshop', 'Art Studio', 17),
    ('2025-05-25 18:00:00', 'Music Jam', 'Practice Room', 18),
    ('2025-05-28 17:00:00', 'Tea Time', 'International House', 18),
    ('2025-05-27 19:00:00', 'Academic Panel', 'Classroom 101', 19),
    ('2025-05-30 18:30:00', 'Game Tournament', 'Game Room', 19),
    -- ('2025-05-29 20:00:00', 'Stargazing', 'Centennial Common', 20),
    ('2025-06-01 15:00:00', 'Picnic', 'West Village Quad', 20),
    ('2025-06-02 18:00:00', 'Resume Workshop', 'Career Center', 21),
    ('2025-06-04 19:00:00', 'Painting Night', 'Art Studio', 21),
    ('2025-06-03 17:30:00', 'Volleyball Game', 'Beach Courts', 22),
    ('2025-06-06 16:00:00', 'Financial Aid Q&A', 'Classroom 202', 22),
    ('2025-06-05 19:30:00', 'Documentary Night', 'Snell Library', 23),
    ('2025-06-08 18:30:00', 'Card Game Night', 'Speare Lounge', 23),
    ('2025-06-07 20:00:00', 'Cooking Contest', 'Smith Kitchen', 24),
    ('2025-06-10 17:00:00', 'Plant Swap', 'Greenhouse', 24),
    ('2025-06-09 15:00:00', 'Language Exchange', 'International House', 25),
    ('2025-06-12 19:00:00', 'Podcast Workshop', 'Media Lab', 25),
    ('2025-06-11 18:00:00', 'Self-Defense Class', 'Marino Center', 26),
    ('2025-06-14 14:00:00', 'Museum Trip', 'Meet at MFA', 26),
    ('2025-06-13 19:30:00', 'Dance Workshop', 'Dance Studio', 27),
    ('2025-06-16 16:30:00', 'Tech Workshop', 'Innovation Center', 27),
    ('2025-06-15 18:00:00', 'Book Exchange', 'Reading Room', 28),
    ('2025-06-18 17:00:00', 'Networking Event', 'Alumni Center', 28),
    ('2025-06-17 19:00:00', 'End-Of-Year Party', 'Curry Center', 29),
    ('2025-06-20 18:30:00', 'Farewell Dinner', 'Faculty Dining', 29),
    ('2025-06-19 20:00:00', 'Outdoor Movie', 'Centennial Common', 30);

-- Complaints (60 complaints) - Weak entity
INSERT INTO complaints VALUES
    (101, 1, 'Noise at midnight'),
    (102, 2, 'Roommate smokes indoors'),
    (103, 3, 'Bathroom cleanliness issues'),
    (104, 4, 'Late night visitors'),
    (105, 5, 'Room temperature too hot'),
    (106, 6, 'Broken window shade'),
    (107, 7, 'Roommate using my things'),
    (108, 8, 'Missing mail package'),
    (109, 9, 'Loud music from neighbors'),
    (110, 10, 'Lack of hot water'),
    (111, 11, 'Heating not working'),
    (112, 12, 'Pest problem'),
    (113, 13, 'Elevator frequently broken'),
    (114, 14, 'Kitchen appliance not working'),
    (115, 15, 'Leaking ceiling'),
    (116, 16, 'Bathroom sink clogged'),
    (117, 17, 'Unstable internet connection'),
    (118, 18, 'Noisy air conditioning'),
    (119, 19, 'Dirty common area'),
    (120, 20, 'Missing furniture'),
    (121, 21, 'Light bulb needs replacement'),
    (122, 22, 'Laundry machine not working'),
    (123, 23, 'People propping doors open'),
    (124, 24, 'Smoking near building entrance'),
    (125, 25, 'Unpleasant odor in hallway'),
    (126, 26, 'Room key not working'),
    (127, 27, 'Roommate conflict over guests'),
    (128, 28, 'Fire alarm going off frequently'),
    (129, 29, 'Insufficient lighting in room'),
    (130, 30, 'People using wrong trash bins'),
    (131, 31, 'Roommate playing loud music'),
    (132, 32, 'Theft from common refrigerator'),
    (133, 33, 'Broken desk chair'),
    (134, 34, 'Ceiling light flickering'),
    (135, 35, 'Roommate sleeping schedule issues'),
    (136, 36, 'Water pressure issues in shower'),
    (137, 37, 'Damaged floor tiles'),
    (138, 38, 'Insufficient cleaning supplies'),
    (139, 39, 'Door doesnt close properly'),
    (140, 40, 'Neighbor cooking with strong odors'),
    (141, 1, 'Roommate conflict over cleanliness'),
    (142, 2, 'Bathroom fan not working'),
    (143, 3, 'Roommate always has guests over'),
    (144, 4, 'Study lounge too noisy'),
    (145, 5, 'No recycling bins available'),
    (146, 6, 'Lost student ID card'),
    (147, 7, 'Roommate leaves food out'),
    (148, 8, 'Broken shower door'),
    (149, 9, 'Water leaking from ceiling'),
    (150, 10, 'Roommate staying up too late'),
    (151, 11, 'Window does not close properly'),
    (152, 12, 'Room needs repainting'),
    (153, 13, 'Radiator makes strange noises'),
    (154, 14, 'Shower temperature fluctuates'),
    (155, 15, 'Roommate not respecting quiet hours'),
    (156, 16, 'Security concern at entrance'),
    (157, 17, 'Room feels drafty'),
    (158, 18, 'Mold in the bathroom'),
    (159, 19, 'Roommate conflict over food sharing'),
    (160, 20, 'Room needs better ventilation');

-- Student-RA Bridge (130 relationships) - Bridge table
INSERT INTO studentBridgeRA VALUES
    (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 2), (7, 2), (8, 2), (9, 2), (10, 2),
    (11, 3), (12, 3), (13, 3), (14, 3), (15, 3), (16, 4), (17, 4), (18, 4), (19, 4), (20, 4),
    (21, 5), (22, 5), (23, 5), (24, 5), (25, 5), (26, 6), (27, 6), (28, 6), (29, 6), (30, 6),
    (31, 7), (32, 7), (33, 7), (34, 7), (35, 7), (36, 8), (37, 8), (38, 8), (39, 8), (40, 8),
    (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (6, 10), (7, 10), (8, 10), (9, 10), (10, 10),
    (11, 11), (12, 11), (13, 11), (14, 11), (15, 11), (16, 12), (17, 12), (18, 12), (19, 12), (20, 12),
    (21, 13), (22, 13), (23, 13), (24, 13), (25, 13), (26, 14), (27, 14), (28, 14), (29, 14), (30, 14),
    (31, 15), (32, 15), (33, 15), (34, 15), (35, 15), (36, 16), (37, 16), (38, 16), (39, 16), (40, 16),
    (1, 17), (2, 17), (3, 17), (4, 17), (5, 17), (6, 18), (7, 18), (8, 18), (9, 18), (10, 18),
    (11, 19), (12, 19), (13, 19), (14, 19), (15, 19), (16, 20), (17, 20), (18, 20), (19, 20), (20, 20),
    (21, 21), (22, 21), (23, 21), (24, 21), (25, 21), (26, 22), (27, 22), (28, 22), (29, 22), (30, 22),
    (31, 23), (32, 23), (33, 23), (34, 23), (35, 23), (36, 24), (37, 24), (38, 24), (39, 24), (40, 24);

-- RA-Event Bridge (130 relationships) - Bridge table
INSERT INTO RABridgeEvents VALUES
    (1, '2025-04-15 18:00:00', 'Pizza Night'),
    (1, '2025-04-20 19:00:00', 'Study Jam'),
    (2, '2025-04-18 17:30:00', 'Game Night'),
    (2, '2025-04-22 16:00:00', 'Career Workshop'),
    (3, '2025-04-17 19:30:00', 'Movie Night'),
    (3, '2025-04-24 18:30:00', 'Yoga Session'),
    (4, '2025-04-16 20:00:00', 'Karaoke Night'),
    (4, '2025-04-23 17:00:00', 'Resume Review'),
    (5, '2025-04-19 15:00:00', 'Campus Tour'),
    (5, '2025-04-25 19:00:00', 'Talent Show'),
    (6, '2025-05-01 18:00:00', 'Cooking Class'),
    (6, '2025-05-03 14:00:00', 'Plant Workshop'),
    (7, '2025-05-02 19:30:00', 'Open Mic Night'),
    (7, '2025-05-05 16:30:00', 'Study Break'),
    (8, '2025-05-04 18:00:00', 'Board Game Night'),
    (8, '2025-05-07 17:00:00', 'Stress Relief'),
    (9, '2025-05-06 19:00:00', 'Cultural Night'),
    (9, '2025-05-09 18:30:00', 'Art Workshop'),
    (10, '2025-05-08 20:00:00', 'Trivia Night'),
    (10, '2025-05-10 15:00:00', 'Sports Watch'),
    (11, '2025-05-12 18:00:00', 'Ice Cream Social'),
    (11, '2025-05-14 19:00:00', 'Meditation'),
    (12, '2025-05-13 17:30:00', 'Job Fair Prep'),
    (12, '2025-05-16 16:00:00', 'Community Service'),
    (13, '2025-05-15 19:30:00', 'Film Screening'),
    (13, '2025-05-18 18:30:00', 'Poetry Reading'),
    (14, '2025-05-17 20:00:00', 'Dance Party'),
    (14, '2025-05-20 17:00:00', 'Fitness Class'),
    (15, '2025-05-19 15:00:00', 'Study Group'),
    (15, '2025-05-22 19:00:00', 'Book Club'),
    (16, '2025-05-21 18:00:00', 'Bowling Night'),
    (16, '2025-05-24 14:00:00', 'Hiking Trip'),
    (17, '2025-05-23 19:30:00', 'Comedy Night'),
    (17, '2025-05-26 16:30:00', 'Craft Workshop'),
    (18, '2025-05-25 18:00:00', 'Music Jam'),
    (18, '2025-05-28 17:00:00', 'Tea Time'),
    (19, '2025-05-27 19:00:00', 'Academic Panel'),
    (19, '2025-05-30 18:30:00', 'Game Tournament'),
    -- (20, '2025-05-29 20:00:00', 'Stargazing'),
    (20, '2025-06-01 15:00:00', 'Picnic'),
    (21, '2025-06-02 18:00:00', 'Resume Workshop'),
    (21, '2025-06-04 19:00:00', 'Painting Night'),
    (22, '2025-06-03 17:30:00', 'Volleyball Game'),
    (22, '2025-06-06 16:00:00', 'Financial Aid Q&A'),
    (23, '2025-06-05 19:30:00', 'Documentary Night'),
    (23, '2025-06-08 18:30:00', 'Card Game Night'),
    (24, '2025-06-07 20:00:00', 'Cooking Contest'),
    (24, '2025-06-10 17:00:00', 'Plant Swap'),
    (25, '2025-06-09 15:00:00', 'Language Exchange'),
    (25, '2025-06-12 19:00:00', 'Podcast Workshop'),
    (26, '2025-06-11 18:00:00', 'Self-Defense Class'),
    (26, '2025-06-14 14:00:00', 'Museum Trip'),
    (27, '2025-06-13 19:30:00', 'Dance Workshop'),
    (27, '2025-06-16 16:30:00', 'Tech Workshop'),
    (28, '2025-06-15 18:00:00', 'Book Exchange'),
    (28, '2025-06-18 17:00:00', 'Networking Event'),
    (29, '2025-06-17 19:00:00', 'End-Of-Year Party'),
    (29, '2025-06-20 18:30:00', 'Farewell Dinner'),
    (30, '2025-06-19 20:00:00', 'Outdoor Movie'),
    (1, '2025-04-18 17:30:00', 'Game Night'),
    (2, '2025-04-15 18:00:00', 'Pizza Night'),
    (3, '2025-04-22 16:00:00', 'Career Workshop'),
    (4, '2025-04-17 19:30:00', 'Movie Night'),
    (5, '2025-04-16 20:00:00', 'Karaoke Night'),
    (6, '2025-04-25 19:00:00', 'Talent Show'),
    (7, '2025-05-01 18:00:00', 'Cooking Class'),
    (8, '2025-05-02 19:30:00', 'Open Mic Night'),
    (9, '2025-05-04 18:00:00', 'Board Game Night'),
    (10, '2025-05-06 19:00:00', 'Cultural Night'),
    (11, '2025-05-08 20:00:00', 'Trivia Night'),
    (12, '2025-05-12 18:00:00', 'Ice Cream Social'),
    (13, '2025-05-13 17:30:00', 'Job Fair Prep'),
    (14, '2025-05-15 19:30:00', 'Film Screening'),
    (15, '2025-05-17 20:00:00', 'Dance Party'),
    (16, '2025-05-19 15:00:00', 'Study Group'),
    (17, '2025-05-21 18:00:00', 'Bowling Night'),
    (18, '2025-05-23 19:30:00', 'Comedy Night'),
    (19, '2025-05-25 18:00:00', 'Music Jam'),
    -- (20, '2025-05-29 20:00:00', 'Stargazing'),
    (21, '2025-06-03 17:30:00', 'Volleyball Game'),
    (22, '2025-06-02 18:00:00', 'Resume Workshop'),
    (23, '2025-06-07 20:00:00', 'Cooking Contest'),
    (24, '2025-06-05 19:30:00', 'Documentary Night'),
    (25, '2025-06-11 18:00:00', 'Self-Defense Class'),
    (26, '2025-06-09 15:00:00', 'Language Exchange'),
    (27, '2025-06-15 18:00:00', 'Book Exchange'),
    (28, '2025-06-13 19:30:00', 'Dance Workshop'),
    (29, '2025-06-19 20:00:00', 'Outdoor Movie'),
    (30, '2025-06-17 19:00:00', 'End-Of-Year Party');

-- RA-Complaint Bridge (130 relationships) - Bridge table
INSERT INTO RABridgeComplaints VALUES
    (1, 101), (1, 102), (1, 103), (1, 104), (1, 105),
    (2, 106), (2, 107), (2, 108), (2, 109), (2, 110),
    (3, 111), (3, 112), (3, 113), (3, 114), (3, 115),
    (4, 116), (4, 117), (4, 118), (4, 119), (4, 120),
    (5, 121), (5, 122), (5, 123), (5, 124), (5, 125),
    (6, 126), (6, 127), (6, 128), (6, 129), (6, 130),
    (7, 131), (7, 132), (7, 133), (7, 134), (7, 135),
    (8, 136), (8, 137), (8, 138), (8, 139), (8, 140),
    (9, 141), (9, 142), (9, 143), (9, 144), (9, 145),
    (10, 146), (10, 147), (10, 148), (10, 149), (10, 150),
    (11, 151), (11, 152), (11, 153), (11, 154), (11, 155),
    (12, 156), (12, 157), (12, 158), (12, 159), (12, 160),
    (13, 101), (14, 102), (15, 103), (16, 104), (17, 105),
    (18, 106), (19, 107), (20, 108), (21, 109), (22, 110),
    (23, 111), (24, 112), (25, 113), (26, 114), (27, 115),
    (28, 116), (29, 117), (30, 118), (1, 119), (2, 120),
    -- (3, 121), (4, 122), (5, 123), (6, 124), (7, 125),
    (8, 126), (9, 127), (10, 128), (11, 129), (12, 130),
    (13, 131), (14, 132), (15, 133), (16, 134), (17, 135),
    (18, 136), (19, 137), (20, 138), (21, 139), (22, 140),
    (23, 141), (24, 142), (25, 143), (26, 144), (27, 145),
    (28, 146), (29, 147), (30, 148), (1, 149), (2, 150),
    (3, 151), (4, 152), (5, 153), (6, 154), (7, 155);
    -- (8, 156), (9, 157), (10, 158), (11, 159), (12, 160);

-- Housing Admins (10 admins) - Strong entity
INSERT INTO housingAdmin VALUES
    (1, 'Jane', 'Doe'),
    (2, 'Mark', 'Lee'),
    (3, 'Elena', 'Vasquez'),
    (4, 'Thomas', 'Wong'),
    (5, 'Amara', 'Johnson'),
    (6, 'Raj', 'Patel'),
    (7, 'Olivia', 'Smith'),
    (8, 'Liam', 'Garcia'),
    (9, 'Zara', 'Chaudry'),
    (10, 'Eli', 'Chen');

-- Conflicts (55 conflicts) - Weak entity
INSERT INTO conflicts VALUES
    (201, TRUE, 1), (202, FALSE, 2), (203, TRUE, 3), (204, FALSE, 4), (205, TRUE, 5),
    (206, FALSE, 6), (207, TRUE, 7), (208, FALSE, 8), (209, TRUE, 9), (210, FALSE, 10),
    (211, TRUE, 1), (212, FALSE, 2), (213, TRUE, 3), (214, FALSE, 4), (215, TRUE, 5),
    (216, FALSE, 6), (217, TRUE, 7), (218, FALSE, 8), (219, TRUE, 9), (220, FALSE, 10),
    (221, TRUE, 1), (222, FALSE, 2), (223, TRUE, 3), (224, FALSE, 4), (225, TRUE, 5),
    (226, FALSE, 6), (227, TRUE, 7), (228, FALSE, 8), (229, TRUE, 9), (230, FALSE, 10),
    (231, TRUE, 1), (232, FALSE, 2), (233, TRUE, 3), (234, FALSE, 4), (235, TRUE, 5),
    (236, FALSE, 6), (237, TRUE, 7), (238, FALSE, 8), (239, TRUE, 9), (240, FALSE, 10),
    (241, TRUE, 1), (242, FALSE, 2), (243, TRUE, 3), (244, FALSE, 4), (245, TRUE, 5),
    (246, FALSE, 6), (247, TRUE, 7), (248, FALSE, 8), (249, TRUE, 9), (250, FALSE, 10),
    (251, TRUE, 1), (252, FALSE, 2), (253, TRUE, 3), (254, FALSE, 4), (255, TRUE, 5);

-- Conflict-Student Bridge (130 relationships) - Bridge table
INSERT INTO conflicts_student VALUES
    (201, 1), (201, 2), (202, 3), (202, 4), (203, 5), (203, 6), (204, 7), (204, 8), (205, 9), (205, 10),
    (206, 11), (206, 12), (207, 13), (207, 14), (208, 15), (208, 16), (209, 17), (209, 18), (210, 19), (210, 20),
    (211, 21), (211, 22), (212, 23), (212, 24), (213, 25), (213, 26), (214, 27), (214, 28), (215, 29), (215, 30),
    (216, 31), (216, 32), (217, 33), (217, 34), (218, 35), (218, 36), (219, 37), (219, 38), (220, 39), (220, 40),
    (221, 1), (221, 3), (222, 5), (222, 7), (223, 9), (223, 11), (224, 13), (224, 15), (225, 17), (225, 19),
    (226, 21), (226, 23), (227, 25), (227, 27), (228, 29), (228, 31), (229, 33), (229, 35), (230, 37), (230, 39),
    (231, 2), (231, 4), (232, 6), (232, 8), (233, 10), (233, 12), (234, 14), (234, 16), (235, 18), (235, 20),
    (236, 22), (236, 24), (237, 26), (237, 28), (238, 30), (238, 32), (239, 34), (239, 36), (240, 38), (240, 40),
    (241, 1), (241, 5), (242, 10), (242, 15), (243, 20), (243, 25), (244, 30), (244, 35), (245, 40), (245, 1),
    (246, 6), (246, 11), (247, 16), (247, 21), (248, 26), (248, 31), (249, 36), (249, 2), (250, 7), (250, 12),
    (251, 17), (251, 22), (252, 27), (252, 32), (253, 37), (253, 3), (254, 8), (254, 13), (255, 18), (255, 23);
    -- (201, 28), (202, 33), (203, 38), (204, 4), (205, 9), (206, 14), (207, 19), (208, 24), (209, 29), (210, 34);

-- Dorm-HousingAdmin Bridge (30 relationships) - Bridge table
INSERT INTO dormBuildingBridgeHousingAdmin VALUES
    (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10),
    (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 1),
    (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8), (7, 9), (8, 10), (9, 1), (10, 2);

-- System Admins (8 admins) - Strong entity
INSERT INTO systemAdmin VALUES
    (1, 'Sam', 'Taylor'),
    (2, 'Alex', 'Smith'),
    (3, 'Jordan', 'Hayes'),
    (4, 'Morgan', 'Rivera'),
    (5, 'Casey', 'Johnson'),
    (6, 'Taylor', 'Kim'),
    (7, 'Riley', 'Patel'),
    (8, 'Jamie', 'Garcia');

-- Clearance Levels (40 clearance levels)
INSERT INTO clearanceLevels VALUES
    (101, 'RA', 'medium'),
    (102, 'HA', 'high'),
    (103, 'Student', 'low'),
    (104, 'SystemAdmin', 'max'),
    (105, 'RA', 'medium'),
    (106, 'HA', 'high'),
    (107, 'Student', 'low'),
    (108, 'SystemAdmin', 'max'),
    (109, 'RA', 'medium'),
    (110, 'HA', 'high'),
    (111, 'Student', 'low'),
    (112, 'RA', 'medium'),
    (113, 'RA', 'medium'),
    (114, 'HA', 'high'),
    (115, 'Student', 'low'),
    (116, 'SystemAdmin', 'max'),
    (117, 'RA', 'medium'),
    (118, 'HA', 'high'),
    (119, 'Student', 'low'),
    (120, 'SystemAdmin', 'max'),
    (121, 'RA', 'medium'),
    (122, 'HA', 'high'),
    (123, 'Student', 'low'),
    (124, 'RA', 'medium'),
    (125, 'RA', 'medium'),
    (126, 'HA', 'high'),
    (127, 'Student', 'low'),
    (128, 'SystemAdmin', 'max'),
    (129, 'RA', 'medium'),
    (130, 'HA', 'high'),
    (131, 'Student', 'low'),
    (132, 'SystemAdmin', 'max'),
    (133, 'RA', 'medium'),
    (134, 'HA', 'high'),
    (135, 'Student', 'low'),
    (136, 'RA', 'medium'),
    (137, 'RA', 'medium'),
    (138, 'HA', 'high'),
    (139, 'Student', 'low'),
    (140, 'SystemAdmin', 'max');

-- SystemAdmin-ClearanceLevel Bridge (130 relationships) - Bridge table
INSERT INTO systemAdminBridgeClearanceLevel VALUES
    (101, 1), (102, 1), (103, 1), (104, 1), (105, 1), (106, 1), (107, 1), (108, 1), (109, 1), (110, 1),
    (111, 2), (112, 2), (113, 2), (114, 2), (115, 2), (116, 2), (117, 2), (118, 2), (119, 2), (120, 2),
    (121, 3), (122, 3), (123, 3), (124, 3), (125, 3), (126, 3), (127, 3), (128, 3), (129, 3), (130, 3),
    (131, 4), (132, 4), (133, 4), (134, 4), (135, 4), (136, 4), (137, 4), (138, 4), (139, 4), (140, 4),
    (101, 5), (102, 5), (103, 5), (104, 5), (105, 5), (106, 5), (107, 5), (108, 5), (109, 5), (110, 5),
    (111, 6), (112, 6), (113, 6), (114, 6), (115, 6), (116, 6), (117, 6), (118, 6), (119, 6), (120, 6),
    (121, 7), (122, 7), (123, 7), (124, 7), (125, 7), (126, 7), (127, 7), (128, 7), (129, 7), (130, 7),
    (131, 8), (132, 8), (133, 8), (134, 8), (135, 8), (136, 8), (137, 8), (138, 8), (139, 8), (140, 8);
    -- (101, 2), (102, 3), (103, 4), (104, 5), (105, 6), (106, 7), (107, 8), (108, 1), (109, 2), (110, 3),
    -- (111, 4), (112, 5), (113, 6), (114, 7), (115, 8), (116, 1), (117, 2), (118, 3), (119, 4), (120, 5),
    -- (121, 6), (122, 7), (123, 8), (124, 1), (125, 2), (126, 3), (127, 4), (128, 5), (129, 6), (130, 7);

-- SystemAdmin-HousingAdmin Bridge (40 relationships) - Bridge table
INSERT INTO systemAdminBridgeHousingAdmin VALUES
    (1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
    (2, 6), (2, 7), (2, 8), (2, 9), (2, 10),
    (3, 1), (3, 3), (3, 5), (3, 7), (3, 9),
    (4, 2), (4, 4), (4, 6), (4, 8), (4, 10),
    (5, 1), (5, 4), (5, 7), (5, 10), (5, 3),
    (6, 2), (6, 5), (6, 8), (6, 1), (6, 4),
    (7, 7), (7, 10), (7, 3), (7, 6), (7, 9),
    (8, 2), (8, 5), (8, 8), (8, 1), (8, 4);

-- SystemAdmin-Conflicts Bridge (130 relationships) - Bridge table
INSERT INTO systemAdminBridgeConflicts VALUES
    (1, 201), (1, 202), (1, 203), (1, 204), (1, 205), (1, 206), (1, 207), (1, 208), (1, 209), (1, 210),
    (2, 211), (2, 212), (2, 213), (2, 214), (2, 215), (2, 216), (2, 217), (2, 218), (2, 219), (2, 220),
    (3, 221), (3, 222), (3, 223), (3, 224), (3, 225), (3, 226), (3, 227), (3, 228), (3, 229), (3, 230),
    (4, 231), (4, 232), (4, 233), (4, 234), (4, 235), (4, 236), (4, 237), (4, 238), (4, 239), (4, 240),
    (5, 241), (5, 242), (5, 243), (5, 244), (5, 245), (5, 246), (5, 247), (5, 248), (5, 249), (5, 250),
    (6, 251), (6, 252), (6, 253), (6, 254), (6, 255), (6, 201), (6, 203), (6, 205), (6, 207), (6, 209),
    (7, 211), (7, 213), (7, 215), (7, 217), (7, 219), (7, 221), (7, 223), (7, 225), (7, 227), (7, 229),
    (8, 231), (8, 233), (8, 235), (8, 237), (8, 239), (8, 241), (8, 243), (8, 245), (8, 247), (8, 249),
    (1, 251), (1, 252), (1, 253), (1, 254), (1, 255), (2, 201), (2, 203), (2, 205), (2, 207), (2, 209),
    (3, 211), (3, 213), (3, 215), (3, 217), (3, 219), (4, 221), (4, 223), (4, 225), (4, 227), (4, 229),
    (5, 231), (5, 233), (5, 235), (5, 237), (5, 239), (6, 241), (6, 243), (6, 245), (6, 247), (6, 249),
    (7, 251), (7, 252), (7, 253), (7, 254), (7, 255), (8, 201), (8, 203), (8, 205), (8, 207), (8, 209);

-- -- Create table for tracking login attempts
-- CREATE TABLE login_attempts (
--     attemptId INT AUTO_INCREMENT,
--     userId INT,
--     timestamp DATETIME,
--     success BOOLEAN,
--     ipAddress VARCHAR(15),
--     PRIMARY KEY (attemptId)
-- );

-- -- Insert sample login attempts
-- INSERT INTO login_attempts (userId, timestamp, success, ipAddress) VALUES
--     (101, '2025-04-15 08:45:22', 0, '192.168.1.45'),
--     (101, '2025-04-15 08:47:15', 0, '192.168.1.45'),
--     (101, '2025-04-15 08:48:30', 0, '192.168.1.45'),
--     (101, '2025-04-15 08:49:45', 0, '192.168.1.45'),
--     (101, '2025-04-15 08:51:12', 1, '192.168.1.45'),
--     (102, '2025-04-15 10:22:18', 0, '10.24.55.82'),
--     (102, '2025-04-15 10:24:32', 0, '10.24.55.82'),
--     (102, '2025-04-15 10:26:45', 0, '10.24.55.82'),
--     (102, '2025-04-15 10:28:17', 1, '10.24.55.82'),
--     (103, '2025-04-15 14:11:05', 0, '172.16.8.201'),
--     (103, '2025-04-15 14:12:30', 0, '172.16.8.201'),
--     (103, '2025-04-15 14:13:45', 0, '172.16.8.201'),
--     (103, '2025-04-15 14:14:22', 1, '172.16.8.201');

-- -- Create table for tracking data access
-- CREATE TABLE data_access_log (
--     logId INT AUTO_INCREMENT,
--     userId INT,
--     dataResource VARCHAR(50),
--     accessType VARCHAR(10), -- 'READ', 'WRITE', 'DELETE'
--     timestamp DATETIME,
--     ipAddress VARCHAR(15),
--     PRIMARY KEY (logId)
-- );

-- -- Insert sample data access logs
-- INSERT INTO data_access_log (userId, dataResource, accessType, timestamp, ipAddress) VALUES
--     (104, 'student_records', 'READ', '2025-04-15 09:22:15', '10.1.5.23'),
--     (108, 'complaints', 'READ', '2025-04-15 10:45:32', '10.1.5.24'),
--     (104, 'conflicts', 'WRITE', '2025-04-15 11:12:47', '10.1.5.23'),
--     (116, 'housingAdmin', 'READ', '2025-04-15 13:35:21', '10.1.5.25'),
--     (132, 'student_records', 'WRITE', '2025-04-15 14:22:18', '10.1.5.26'),
--     (128, 'preferences', 'READ', '2025-04-15 15:50:33', '10.1.5.27'),
--     (104, 'dorm_room', 'WRITE', '2025-04-15 16:42:31', '10.1.5.23'),
--     (140, 'events', 'READ', '2025-04-15 17:15:42', '10.1.5.28'),
--     (120, 'applications', 'WRITE', '2025-04-15 09:33:15', '10.1.5.29'),
--     (112, 'clearanceLevels', 'READ', '2025-04-15 10:17:22', '10.1.5.30');

-- -- Create table for tracking system maintenance
-- CREATE TABLE system_maintenance (
--     maintenanceId INT AUTO_INCREMENT,
--     type VARCHAR(50),
--     scheduleTime DATETIME, 
--     completionTime DATETIME,
--     status VARCHAR(20),
--     details VARCHAR(200),
--     PRIMARY KEY (maintenanceId)
-- );

-- -- Insert sample maintenance records
-- INSERT INTO system_maintenance (type, scheduleTime, completionTime, status, details) VALUES
--     ('Database Backup', '2025-04-15 02:00:00', '2025-04-15 02:15:22', 'Completed', 'Routine daily backup'),
--     ('Security Update', '2025-04-10 01:00:00', '2025-04-10 03:25:14', 'Completed', 'April security patches'),
--     ('System Restart', '2025-04-05 02:00:00', '2025-04-05 02:10:45', 'Completed', 'Monthly maintenance restart'),
--     ('Database Optimization', '2025-04-01 01:30:00', '2025-04-01 02:45:12', 'Completed', 'Index rebuilding and table optimization'),
--     ('Backup Verification', '2025-03-25 03:00:00', '2025-03-25 04:15:33', 'Completed', 'Quarterly backup integrity check');

-- -- Create table for permissions audit
-- CREATE TABLE permission_changes (
--     changeId INT AUTO_INCREMENT,
--     timestamp DATETIME,
--     changedBy INT,
--     targetUser INT,
--     action VARCHAR(100),
--     oldRole VARCHAR(30),
--     newRole VARCHAR(30),
--     PRIMARY KEY (changeId)
-- );

-- -- Insert sample permission changes
-- INSERT INTO permission_changes (timestamp, changedBy, targetUser, action, oldRole, newRole) VALUES
--     ('2025-04-15 10:23:45', 104, 117, 'Changed role', 'Student', 'RA'),
--     ('2025-04-14 16:42:31', 104, 123, 'Added new user', NULL, 'Housing Admin'),
--     ('2025-04-13 14:15:22', 108, 131, 'Changed clearance level', 'RA', 'RA'),
--     ('2025-04-12 11:33:47', 116, 118, 'Deactivated account', 'Student', NULL),
--     ('2025-04-11 09:22:15', 128, 125, 'Changed role', 'RA', 'Housing Admin'),
--     ('2025-04-10 15:42:33', 104, 115, 'Changed clearance level', 'Student', 'Student'),
--     ('2025-04-09 14:17:28', 140, 112, 'Reactivated account', NULL, 'RA'),
--     ('2025-04-08 16:33:44', 116, 140, 'Changed role', 'RA', 'System Admin');

-- -- Sample queries for different personas

-- -- View dorm locations and availability (Bob - Student)
-- SELECT dormId, name, address, numRooms, occupancy, maxCapacity, bedsAvailable, amenities 
-- FROM dormBuilding;

-- -- View detailed information about each dorm (Bob - Student)
-- SELECT d.dormId, d.name, d.address, d.numRooms, d.occupancy, d.bedsAvailable, d.amenities,
--        COUNT(dr.roomNum) as occupied_rooms
-- FROM dormBuilding d
-- JOIN dorm_room dr ON d.dormId = dr.dormId
-- WHERE dr.stuId IS NOT NULL
-- GROUP BY d.dormId;

-- -- Access resident contact info for an RA (Renee - RA)
-- SELECT s.stuId, s.firstName, s.lastName, e.email
-- FROM student s
-- JOIN student_email e ON s.stuId = e.stuId
-- JOIN studentBridgeRA sr ON s.stuId = sr.stuId
-- WHERE sr.raId = 1;

-- -- View anonymous complaints from students (Renee - RA)
-- SELECT c.compId, c.description
-- FROM complaints c
-- JOIN RABridgeComplaints rc ON c.compId = rc.compId
-- WHERE rc.raId = 1;

-- -- View overview of complaints and events (Renee - RA)
-- SELECT c.compId, c.description, e.title, e.datetime
-- FROM complaints c
-- JOIN RABridgeComplaints rc ON c.compId = rc.compId
-- JOIN events e ON rc.raId = e.raId
-- WHERE rc.raId = 1
-- ORDER BY e.datetime;

-- -- View all events for an RA in calendar order (Renee - RA)
-- SELECT e.title, e.datetime, e.location 
-- FROM events e
-- JOIN RABridgeEvents re ON e.datetime = re.datetime AND e.title = re.title
-- WHERE re.raId = 1 
-- ORDER BY e.datetime ASC;

-- -- Count of roommate conflicts per dorm (Jane - Housing Admin)
-- SELECT db.dormId, db.name, COUNT(cs.confId) AS conflict_count
-- FROM dormBuilding db
-- JOIN dorm_room dr ON db.dormId = dr.dormId
-- JOIN conflicts_student cs ON cs.studentId = dr.stuId
-- JOIN conflicts c ON c.confId = cs.confId
-- GROUP BY db.dormId, db.name
-- ORDER BY conflict_count DESC;

-- -- View roommate match success rates per dorm (Jane - Housing Admin)
-- SELECT db.dormId, db.name, 
--        COUNT(DISTINCT dr.stuId) AS total_students,
--        COUNT(DISTINCT cs.confId) AS conflicts,
--        (1 - (COUNT(DISTINCT cs.confId) / COUNT(DISTINCT dr.stuId))) * 100 AS success_rate
-- FROM dormBuilding db
-- LEFT JOIN dorm_room dr ON db.dormId = dr.dormId
-- LEFT JOIN conflicts_student cs ON cs.studentId = dr.stuId
-- WHERE dr.stuId IS NOT NULL
-- GROUP BY db.dormId, db.name
-- ORDER BY success_rate DESC;

-- -- Summary report of dorm building stats (Jane - Housing Admin)
-- SELECT db.dormId, db.name, db.numRooms, db.occupancy, db.maxCapacity, db.bedsAvailable,
--        (db.occupancy / db.maxCapacity) * 100 AS occupancy_rate
-- FROM dormBuilding db
-- ORDER BY occupancy_rate DESC;

-- -- View all users and their roles/clearance levels (Sam - System Admin)
-- SELECT cl.userId, cl.role, cl.clearance,
--        CASE 
--          WHEN cl.role = 'RA' THEN (SELECT CONCAT(firstName, ' ', lastName) FROM RA WHERE raId = cl.userId)
--          WHEN cl.role = 'HA' THEN (SELECT CONCAT(firstName, ' ', lastName) FROM housingAdmin WHERE haId = cl.userId)
--          WHEN cl.role = 'Student' THEN (SELECT CONCAT(firstName, ' ', lastName) FROM student WHERE stuId = cl.userId)
--          WHEN cl.role = 'SystemAdmin' THEN (SELECT CONCAT(firstName, ' ', lastName) FROM systemAdmin WHERE adminId = cl.userId)
--          ELSE 'Unknown'
--        END AS fullName
-- FROM clearanceLevels cl
-- ORDER BY cl.role, cl.clearance;

-- -- View system admins and the complaints they can access (Sam - System Admin)
-- SELECT sa.adminId, sa.firstName, sa.lastName, COUNT(sc.confId) AS accessible_conflicts
-- FROM systemAdmin sa
-- LEFT JOIN systemAdminBridgeConflicts sc ON sa.adminId = sc.adminId
-- GROUP BY sa.adminId, sa.firstName, sa.lastName
-- ORDER BY accessible_conflicts DESC;

-- -- View recent suspicious login activity (Sam - System Admin)
-- SELECT userId, 
--        COUNT(*) AS failed_attempts, 
--        MAX(timestamp) AS last_attempt,
--        ipAddress
-- FROM login_attempts
-- WHERE success = 0
-- GROUP BY userId, ipAddress
-- HAVING COUNT(*) > 2
-- ORDER BY failed_attempts DESC;

-- -- View system maintenance schedule (Sam - System Admin)
-- SELECT type, scheduleTime, completionTime, status, details,
--        TIMESTAMPDIFF(MINUTE, scheduleTime, completionTime) AS duration_minutes
-- FROM system_maintenance
-- ORDER BY scheduleTime DESC;

-- -- View recent permission changes (Sam - System Admin)
-- SELECT pc.timestamp, 
--        pc.action,
--        (SELECT CONCAT(firstName, ' ', lastName) FROM systemAdmin WHERE adminId = pc.changedBy) AS changed_by,
--        pc.oldRole,
--        pc.newRole
-- FROM permission_changes pc
-- ORDER BY pc.timestamp DESC;