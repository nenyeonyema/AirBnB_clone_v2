-- setup_mysql_test.sql
-- Creates a MySQL server with:
--   Database hbnb_test_db.
--   User hbnb_test with password hbnb_test_pwd in localhost.
--   Grants all privileges for hbnb_test on hbnb_test_db.
--   Grants SELECT privilege for hbnb_test on performance_schema.

-- Creates the database hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- add the user hbnb_test identified with password 'hbnb_test_pwd'
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- add privileges to hbnb_test
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
-- refresh to apply privileges
-- FLUSH PRIVILEGES;
