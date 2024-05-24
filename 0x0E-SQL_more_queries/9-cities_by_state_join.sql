-- Creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server
SELECT cities.id, cities.name, states.name
FROM cities JOIN states
WHERE cities.state_id = states.id
ORDER BY cities.state_id;