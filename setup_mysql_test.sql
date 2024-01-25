-- Create a database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create a user if it doesn't already exist and set its password
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on the hbnb_dev_db database to the hbnb_dev user
GRANT ALL ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';