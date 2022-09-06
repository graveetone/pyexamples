-- https://www.programiz.com/sql/online-compiler/
  
--SELECT * FROM Customers;
SELECT COUNT(customer_id) FROM (SELECT * FROM Customers JOIN Orders); --декартовий добуток кожен з кожним
SELECT * FROM Customers JOIN Orders WHERE Customers.customer_id = Orders.customer_id; -- хто що купував
SELECT * FROM Orders LEFT JOIN Customers WHERE Customers.customer_id == Orders.customer_id;
-- LEFT - всі з лівої таблиці + всі можливі з правої таблиці
-- RIGHT - всі з правої таблиці + всі можливі з лівої таблиці
-- table1 LEFT table2 те ж саме, що table2 RIGHT table1
-- OUTER 

-- https://www.geeksforgeeks.org/sql-join-set-1-inner-left-right-and-full-joins/