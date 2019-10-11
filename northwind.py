import sqlite3


conn = sqlite3.connect('northwind_small.sqlite3')
c = conn.cursor()

c.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;").fetchall()
print(c.execute("SELECT UnitPrice FROM Product ORDER BY UnitPrice DESC LIMIT 10;").fetchall()) # Top 10 most expensive items
print(c.execute(" SELECT AVG(HireDate - BirthDate) AS Age FROM Employee;").fetchone())  #Avg Age: 37.222

# Part 3
print(c.execute("SELECT SupplierName, UnitPrice, ProductName FROM ProductDetails_VORDER BY UnitPrice DESC LIMIT 10;"))
print(c.execute("SELECT MAX(CategoryName) FROM ProductDetails_V;")) # Largest Catergory is Seafood.
conn.commit()
conn.close()
