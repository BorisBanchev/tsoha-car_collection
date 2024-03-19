DROP TABLE IF EXISTS garages CASCADE;
DROP TABLE IF EXISTS cars CASCADE;
DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS garagecars CASCADE;
DROP TABLE IF EXISTS usercars CASCADE;
DROP TABLE IF EXISTS usergarages CASCADE;


CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT
);

CREATE TABLE garages (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    capacity INTEGER NOT NULL
);

CREATE TABLE cars (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);  

CREATE TABLE garagecars (
    id SERIAL PRIMARY KEY,
    garage_id INTEGER REFERENCES garages(id),
    car_id INTEGER REFERENCES cars(id)
);  

CREATE TABLE usercars (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    car_id INTEGER REFERENCES cars(id)
);  

CREATE TABLE usergarages (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    garage_id INTEGER REFERENCES garages(id)
);  