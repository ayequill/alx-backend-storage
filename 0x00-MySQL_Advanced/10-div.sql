-- An sql function that divides two numbers
DELIMITER $$

CREATE FUNCTION SafeDiv(upper INT, lower INT)
RETURNS FLOAT
    DETERMINISTIC
BEGIN
    IF lower = 0 THEN
        RETURN 0;
    END IF;
    RETURN upper / lower;
END;
$$

DELIMITER ;