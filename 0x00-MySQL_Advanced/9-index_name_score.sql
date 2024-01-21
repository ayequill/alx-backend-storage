-- Create an index idx_name_first_score
-- on table names and first letter and the score
CREATE INDEX idx_name_first_score ON names(name(1), score);
