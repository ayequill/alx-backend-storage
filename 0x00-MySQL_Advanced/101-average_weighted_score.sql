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

    forEachUser: LOOP
        FETCH user INTO user_id;

        IF user_id IS NULL THEN
            LEAVE forEachUser;
        END IF;

        SELECT sum(score * weight) / sum(weight) INTO avg
        FROM corrections JOIN projects proj ON proj.id = corrections.project_id
        WHERE id = user_id;
    END LOOP;
    CLOSE user;
END ##
DELIMITER ;