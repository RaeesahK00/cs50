--Query to view the list of all movies released in 2010 and their ratings,(title of each movie and the rating)
--in descending order by rating. For movies with the same rating, order them alphabetically by title.
SELECT DISTINCT movies.title, ratings.rating
FROM ratings
JOIN movies ON ratings.movie_id = movies.id
WHERE year = 2010
ORDER BY rating DESC, movies.title;
