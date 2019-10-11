## Questions - Part 1
1. Count how many rows you have - it should be 3!
```python 
    for row in c.execute('SELECT * FROM demo;'):
        print(row)
```
We can assure that there are three rows. 

2. How many unique values of y are there (hint - COUNT() can accept a keyword DISTINCT)?
```python
y = c.execute('SELECT COUNT(DISTINCT y) FROM demo;') # 2 distict values. 
print(c.fetchone())
```

## Questions - Part 2
1. What are the ten most expensive items (per unit price) in the database?
    1.  263.5    côte de Blaye
    2.  123.79   Thüringer Rostbratwurst
    3.  97	     Mishi Kobe Niku
    4.  81	     Sir Rodney's Marmalade
    5.  62.5     Carnarvon Tigers
    6.  55       Raclette Courdavault
    7.  53	     Manjimup Dried Apples
    8.  49.3     Tarte au sucre
    9.  46	     Ipoh Coffee
    10. 45.6   	 Rössle Sauerkraut
2. What is the average age of an employee at the time of their hiring? (Hint: a lot of arithmetic works with dates.)
    * Avg Age: 37.222

## Questions - Part 3
1. What are the ten most expensive items (per unit price) in the database and their suppliers?
    1. Aux joyeux ecclésiastiques	263.5	Côte de Blaye
    2. Plutzer Lebensmittelgroßmärkte AG	123.79	Thüringer Rostbratwurst
    3. Tokyo Traders	97	Mishi Kobe Niku
    4. Specialty Biscuits, Ltd.	81	Sir Rodney's Marmalade
    5. Pavlova, Ltd.	62.5	Carnarvon Tigers
    6. Gai pâturage	55	Raclette Courdavault
    7. G'day, Mate	53	Manjimup Dried Apples
    8. Forêts d'érables	49.3	Tarte au sucre
    9. Leka Trading	46	Ipoh Coffee
    0. Plutzer Lebensmittelgroßmärkte AG	45.6	Rössle Sauerkraut
2. What is the largest category (by number of unique products in it)?
    * Seafood at 8 items in the category. 
    
## Questions - Part 4
1. In the Northwind database, what is the type of relationship between the Employee and Territory tables?
    * Every employee is connected to terrories table via the EmployeeID that meets in the EmployeeTerritories table. 
2. What is a situation where a document store (like MongoDB) is appropriate, and what is a situation where it is not appropriate?
    * Depending on the usecase, MongoDB can be used to quickly build up applications or databases without much care. Examples are like building
    an MVP. It's easier to use, connections are fast and usually allows larger storage options than some of the other options like PostgreSQL.
3. What is "NewSQL", and what is it trying to achieve?
    * Is a newer approach to databases. It's job is to combine the horizontal scalability of NoSQL databases while also guranteeing ACID in it's databases. 
    While there are still cases of use for NoSQL, the people behind NewSQL just want the best of both worlds. In a  nutshell they are trying to make a new standard.
