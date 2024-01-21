-- A stored procedure to compute weighted average
-- obtained by a student
DELIMITER ##

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(userID INT)
BEGIN
    DECLARE avg FLOAT;
    SELECT SUM(score * weight) / SUM(weight)
    INTO avg
    FROM corrections
             JOIN projects p ON p.id = project_id
    WHERE userID = user_id;

    UPDATE users
    SET average_score = avg
    WHERE id = userID;
END;
##

DELIMITER ;