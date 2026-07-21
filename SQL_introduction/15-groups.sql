-- This script lists the number of records with the same score in second_table
-- Command to group records by score and display count ordered by number descending
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
