
-- SCRIPT TO EXECUTE SQL CODE INSIDE pg_container/week1 database
-- cat week2_script.sql | docker exec -i pg_container psql -d week2

-- OPEN psql interactive shell and input SQL commands
-- docker exec -it pg_container psql northwind

-- CC: DATABASE MANIPULATION W/ SQL
-- DROP TABLE divisions, teams;
-- CREATE TABLE divisions(
--     id SERIAL,
--     name TEXT NOT NULL UNIQUE,
--     PRIMARY KEY(id)
-- );

-- CREATE TABLE teams(
--     id SERIAL,
--     city TEXT NOT NULL,
--     name TEXT NOT NULL UNIQUE,
--     home_color TEXT NOT NULL,
--     away_color TEXT,
--     division_id INT,
--     PRIMARY KEY(id)
-- );

-- ALTER TABLE teams 
-- ADD CONSTRAINT fk_teams_divisions 
-- FOREIGN KEY (division_id) 
-- REFERENCES divisions (id) 
-- ON DELETE SET NULL;

-- INSERT INTO divisions (name)
-- VALUES 
-- ('Atlantic'),
-- ('Metropolitan'),
-- ('Pacific'),
-- ('Central');

-- INSERT INTO teams (city,name,home_color,away_color,division_id)
-- VALUES 
-- ('New York','Islanders','Royal blue','White',2),
-- ('Seattle', 'Kraken', 'Deep sea blue','White',3);

-- UPDATE divisions set name = 'Cosmopolitan'
-- WHERE name = 'Metropolitan';

-- DELETE FROM divisions
-- WHERE name = 'Cosmopolitan';

-- END CC--------------------


-- EXERCISE --------------------
-- SELECT city,name FROM teams WHERE name = 'Kraken' OR name = 'Islanders';
-- SELECT city,name,home_color FROM teams WHERE name = 'Kraken' AND city = 'Seattle';

-- SELECT title AS book_title, year AS book_year FROM books
-- WHERE title LIKE 'B%'
-- ORDER BY book_year ;
-- EXERCISE END -----------------



-- CC : DATABASE QUERIES
-- 1.
-- SELECT DISTINCT company_name FROM customers 
-- WHERE company_name >= 'Q'
-- ORDER BY company_name DESC;
-- 2.
-- SELECT first_name, last_name FROM employees
-- WHERE title = 'Sales Representative'
-- ORDER BY last_name, first_name;
-- 3.
-- SELECT first_name, home_phone FROM employees 
-- WHERE first_name LIKE 'A%' AND home_phone LIKE '%4%' 
-- ORDER BY employee_id;

-- END CC--------------------

-- EXCERCISE-----------------
-- SELECT MAX(year) FROM books;
-- SELECT genre, COUNT(*) FROM books
-- GROUP BY genre
-- HAVING COUNT(*)>1;
-- EXERCISE END -----------------



-- CC : AGGREGATE QUERIES ------
-- 1. 
-- SELECT customer_id, MIN(order_date) FROM orders
-- GROUP BY customer_id
-- ORDER BY customer_id
-- 2.
-- SELECT customer_id, AVG(freight) AS avg_freight FROM orders
-- GROUP BY customer_id
-- ORDER BY avg_freight;
-- 3. REVIEW
SELECT o.order_id, count(DISTINCT product_id) AS product_count 
FROM order_details o 
GROUP BY order_id HAVING(count(*)) >= 5 
ORDER BY product_count DESC;








