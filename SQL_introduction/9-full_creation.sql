-- This script creates a table second_table and inserts multiple rows
-- Command to create second_table if it does not exist
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- Command to insert initial records into second_table
INSERT INTO second_table (id, name, score)
    (1, 'John', 10),
    (2, 'Alex', 3),
    (3, 'Bob', 14),
    (4, 'George', 8);
