--Viewing all the names of the songs where the ID is linked to Post Malone
SELECT name
FROM songs
WHERE artist_id =
(
    SELECT id
    FROM artists
    WHERE name = 'Post Malone'
);
