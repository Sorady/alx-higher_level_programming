-- Creates the database hbtn_0d_usa and the table hbtn_0d_usa.cities
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;

CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`cities` (
	id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
	state_id INT NOT NULL,
	name VARCHAR(256),
	FOREIGN KEY (state_id) REFERENCES states(id)
);
