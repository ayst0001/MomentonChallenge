# MomentonChallenge
Momenton Code Challenge - solution by Ray Wang

# Assumptions
1. The popularity of a genre is defined by the average rating of any rating records available regarding any movie classified as this genre
2. Different combinations of sub-genres are considered as different genres - e.g. Action|Short, Action, Short are considered as 3 different genres
3. For a genre to be eligible for this "popularity contest", movies of this genre have to be rated frequently. As a result, in the final answer, only the genres ranking top 10 in rating frequency each year were included. Without this rule, niche market movies with only one crazy fan giving a 10/10 would often stand out. 

# Solutions implemented
1. Pipeline for raw .dat -> BigQuery: used timestamp.py to handle timestamps in ratings.dat, mainly for extracting the "year" of ratings. I also used Cloud Dataprep to generate Cloud DataFlow jobs for ETL.
2. Load the output files of 1 from GCS output location into BigQuery as 3 tables
3. Query the 3 tables with query.sql to generate results for each year between 2013-2019

# Advantages of this approach
1. Reusable analytics platform - should we have to provide other insight with the same dataset, we can simply run a different SQL query against the tables and the response time is in seconds
2. Highly scalable ETL pipeline 
3. Fast dev to prod cycle - no need to write DataFlow job from scratch since the data is fairly structured and of decent quality

# Potential issues and improvement
1. This solution did not take into consideration that the same combination of sub-genres can appear in different orders. i.e. Short|Comedy and Comedy|Short are considered as different genres. The reason is that the order of each sub-genres may have a meaning, e.g. representing the order of significance of the correlation between each sub-genre and the movie. However, if this is not the case, then a sorting step for this genre field should be implemented in the ETL logic. 
2. This solution does not handle much data quality issues from the raw data. Ideally in the ETL logic, good records and bad records should go to different target and we should only utilize good record for generating the insight
3. In the SQL I used a "like" clause and wildcard to isolate records for each year, this could have been handled more percisly in the ETL logic. 
4. "count_movies" columns in the results are a bit confusing, should have been renamed into "count_ratings"
