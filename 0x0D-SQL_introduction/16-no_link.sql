-- deletes the database hbtn_0c_0
SELECT score, name FROM second_table
WHERE name NOT NULL
GROUP BY score ASC;
