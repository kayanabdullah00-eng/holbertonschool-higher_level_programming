-- This script lists all records with a score >= 10 in second_table
-- Command to select score and name where score is at least 10, ordered by score descending
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
