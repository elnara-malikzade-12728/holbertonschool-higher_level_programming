-- lists all records of the table excluding null
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
