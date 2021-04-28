CREATE DATABASE test;

USE test;

CREATE TABLE MyGuests (
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
firstname VARCHAR(30) NOT NULL,
lastname VARCHAR(30) NOT NULL
);


DELIMITER //
CREATE PROCEDURE add_guest (IN first varchar(30), IN last varchar(30))
BEGIN
INSERT INTO MyGuests (firstname,lastname)VALUES (first, last);
END//
DELIMITER ;

-- DROP PROCEDURE add_guest;

-- call add_guest('Jan','Czerwiec');
-- select * from MyGuests;

DELIMITER //
CREATE PROCEDURE delete_guest ( identificator INT)
BEGIN
DELETE FROM MyGuests WHERE MyGuests.id = identificator;
END//
DELIMITER ;
-- call delete_guest(2);

DELIMITER //
CREATE PROCEDURE update_record (IN identificator INT, first varchar(30), IN last varchar(30))
BEGIN
UPDATE MyGuests
SET MyGuests.firstname = first, MyGuests.lastname=last
WHERE MyGuests.id = identificator;
END//
DELIMITER ;

-- DROP PROCEDURE update_record;

-- call update_record(1,'Jan','Kwiecien');
