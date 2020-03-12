# MomentonChallenge
Momenton Code Challenge - solution of Ray Wang

# Asumptions
1. Popularity of a genre is defined by average rating of any rating records available regarding any movie classified as this genre
2. Different combaination of sub-genres are considered as different genres - e.g. Action|Short, Action, Short will be considered as 3 different genres
3. For a genre to be eligible for this "popularity contest", movies of this genre have to be rated frequently. As a result in the final results only the top 10 rated genre each year were included. Without this rule, niche market movies with only one crazy fan giving a 10/10 would stand out. 

#Solutions implemented:
1. Prepare data for BigQuery - used timestamp.py to handle timestamps in ratings.dat, mainly to for extracting in which year the rating was made. Also used Cloud Dataprep to generate Cloud DataFlow jobs for ETL.
2. Load the output files of 1 from GCS output location into BigQuery as 3 tables
3. Query the 3 tables with query.sql to generate results for each year

