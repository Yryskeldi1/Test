CREATE DATABASE jorgotaxi;
CREATE TABLE cars;
CREATE TABLE driver;
CREATE TABLE call_centr;
SELECT * FROM cars WHERE make = 'Toyota' AND model = 'Camry' ORDER BY DESC;
SELECT DISTINCT name FROM call_centr ORDER BY name DESC LIMIT 10;
UPDATE cars SET make = 'Mersus' WHERE make = 'Mersedes';
DELETE * FROM driver WHERE first_name = 'Azamat' AND last_name ='Azamatov';
SELECT * FROM driver WHERE experience > 10 AND gender = 'female';
SELECT AVG(experience) FROM driver WHERE data_birth > '1975-10-10';
SELECT * FROM driver JOIN cars ON driver.id_car = cars.id;
SELECT COUNT ('BMW','Mercedes','Toyota') FROM cars ORDER BY DESC;