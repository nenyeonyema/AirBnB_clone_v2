-- setup_mysql_test.sql

-- Create or use hbnb_test_db database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create or use hbnb_test user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant privileges on hbnb_test_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Show privileges for the user
SHOW GRANTS FOR 'hbnb_test'@'localhost';
