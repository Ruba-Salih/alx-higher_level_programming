-- Creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server
SELECT tv_genres.name AS genre, tv_genres.id AS number_of_shows
FROM tv_genres JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
ORDER BY genre , number_of_shows DESC;