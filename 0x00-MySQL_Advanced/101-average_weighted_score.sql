-- A stored procedure to compute weighted average
-- obtained by a student
DELIMITER ##

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE avg FLOAT;
    DECLARE user_id INT;
    DECLARE user CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET user_id = NULL;

    OPEN user;

    forEachUser:
    LOOP
        FETCH user INTO user_id;

        IF user_id IS NULL THEN
            LEAVE forEachUser;
        END IF;

        SELECT SUM(score * weight) / SUM(weight)
        INTO avg
        FROM corrections
                 INNER JOIN projects ON id = project_id
        WHERE id = user_id;

        UPDATE users
        SET average_score = avg
        WHERE user_id = id;
    END LOOP;
    CLOSE user;
END ##
DELIMITER ;