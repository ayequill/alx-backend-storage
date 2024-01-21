-- A stored procedure to compute weighted average
-- obtained by a student
DELIMITER ##

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE avg FLOAT;
    DECLARE userID INT;
    DECLARE user CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET userID = NULL;

    OPEN user;

    forEachUser:
    LOOP
        FETCH user INTO userID;

        IF userID IS NULL THEN
            LEAVE forEachUser;
        END IF;

        SELECT SUM(score * weight) / SUM(weight)
        INTO avg
        FROM corrections
                 INNER JOIN projects ON id = project_id
        WHERE userID = user_id;

        UPDATE users
        SET average_score = avg
        WHERE id = userID;
    END LOOP;
    CLOSE user;
END ##
DELIMITER ;