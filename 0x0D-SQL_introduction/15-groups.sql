-- deletes the database hbtn_0c_0
SELECT score, COUN(score) AS number FROM second_table
WHERE score = score
GROUP BY score;
