-- script that creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student.

DELIMITER EOF
CREATE PROCEDURE ComputeAverageScoreForUser(users_id INT)
BEGIN
    DECLARE avg FLOAT;
    SELECT AVG(score) INTO avg FROM corrections WHERE user_id = users_id;

    UPDATE users
    SET average_score = avg
    WHERE id = users_id;
END;
EOF
DELIMITER ;
