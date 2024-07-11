-- Create a trigger that reset valid_email
-- only if email has been changed
DELIMITER $$
CREATE TRIGGER before_email_update
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END$$
DELIMITER ;

