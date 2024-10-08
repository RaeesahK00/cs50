--Viewing all the names of the songs that have a featured artist in them.
SELECT name
FROM songs
WHERE name LIKE '%feat%';
