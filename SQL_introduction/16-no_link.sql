-- lists all records of the table excluding null
INSERT INTO second_table (id, name, score) VALUES (5, 'Aria', 12), (6, 'Aria', 18);
SELECT score, name FROM second_table WHERE name IS NOT NULL AND score >= 10 ORDER BY score DESC;
