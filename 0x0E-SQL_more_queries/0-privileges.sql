CREATE USER 'user_0d_1'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

CREATE USER 'user_0d_2'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost';

SELECT * FROM mysql.user WHERE User IN ('user_0d_1', 'user_0d_2') AND Host = 'localhost';
