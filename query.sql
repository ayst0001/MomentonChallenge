select * from(
select * from(
select genres, AVG(R.rating) as average_rating, count(genres) as count_movies from (
select * from momenton_movies.ratings where rating_timestamp like '%2019') as R
join 
(select * from momenton_movies.movies) AS M
on R.movie_id = M.movie_id
group by genres
) order by count_movies DESC limit 10
) order by average_rating DESC;
