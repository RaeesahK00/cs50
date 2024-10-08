--Viewing all the names of the songs from the database where danceability, energy and valence is greater than 0.75.
SELECT name FROM songs WHERE danceability > 0.75 AND energy > 0.75 AND valence > 0.75;
