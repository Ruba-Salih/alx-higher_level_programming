-- Creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows INNER JOIN tv_show_genres
WHERE tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC AND tv_show_genres.genre_id;