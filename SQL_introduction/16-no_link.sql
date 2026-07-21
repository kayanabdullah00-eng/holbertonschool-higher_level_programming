-- This script lists all records of second_table having a name value
-- Command to select score and name where name is valid, ordered by score descending
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
