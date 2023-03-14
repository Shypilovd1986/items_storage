CREATE TABLE brands(
    brand_id INT(10) NOT NULL AUTO_INCREMENT,
    brand_name VARCHAR(15) NOT NULL,
    country_of_origin VARCHAR(15)  NOT NULL,
    PRIMARY KEY(brand_id)
);


CREATE TABLE items(
    item_id INT(10) NOT NULL UNIQUE,
    item_name VARCHAR(15) NOT NULL,
    item_colour VARCHAR(15) NOT NULL,
    price FLOAT NOT NULL,
    date_of_production DATE NOT NULL,
    brand_id INT(10) NOT NULL,
    PRIMARY KEY(item_id),
    FOREIGN KEY(brand_id) REFERENCES brands(brand_id)
);

INSERT INTO brands(brand_name, country_of_origin) VALUES ('Shneider electric', 'France');

INSERT INTO items(item_id, item_name, item_colour, price, date_of_production, brand_id)
VALUES(234424352, 'socket', 'black', 3.10, NOW(),1);

ALTER TABLE brands MODIFY COLUMN brand_name VARCHAR(20) NOT NULL UNIQUE;