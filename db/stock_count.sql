DROP TABLE IF EXISTS stock;
DROP TABLE IF EXISTS manufacturers;

CREATE TABLE manufacturers(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255)
);

CREATE TABLE stock(
    id SERIAL PRIMARY KEY, 
    name VARCHAR(255),
    description VARCHAR(255),
    cost INT,
    peice INT,
    in_stock BOOLEAN,
    manufacturers_id INT REFERENCES manufacturers(id) ON DELETE CASADE
);