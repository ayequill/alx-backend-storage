--  creates a stored procedure AddBonus that adds a new correction for a student.
-- user_id corresponds to the user id.
-- project_name corresponds to a project or create a new project if it does not exist.
-- score is the value of the correction.
DELIMITER $$
CREATE PROCEDURE AddBonus(user_id INT, project_name VARCHAR(255), score INT)
BEGIN
    DECLARE projId INT DEFAULT -1;

    SELECT id INTO projId FROM projects WHERE name = project_name;
    IF projId = -1 THEN
        INSERT INTO projects (name) VALUES (project_name);
        SET projId = LAST_INSERT_ID();
    END IF;

    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, projId, score);
END;
$$
DELIMITER ;
