import sqlite3
import pandas as pd

# Connect to SQLite database (creates it if it doesn't exist)
conn = sqlite3.connect('example8.db')
cursor = conn.cursor()

# Create the Employee table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Employee (
    id INTEGER PRIMARY KEY,
    name TEXT,
    salary INTEGER,
    departmentId INTEGER,
    FOREIGN KEY(departmentId) REFERENCES Department(id)
);
""")

# Create the Department table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Department (
    id INTEGER PRIMARY KEY,
    name TEXT  
);
""")

# Insert sample data into Employee table (uncomment to run once)
cursor.execute("INSERT OR IGNORE INTO Department (id, name) VALUES (1, 'IT'), (2, 'Sales')")
cursor.execute("INSERT OR IGNORE INTO Employee (name, salary, departmentId) VALUES ('Joe', 70000, 1);")
cursor.execute("INSERT OR IGNORE INTO Employee (name, salary, departmentId) VALUES ('Jim', 90000, 1);")
cursor.execute("INSERT OR IGNORE INTO Employee (name, salary, departmentId) VALUES ('Henry', 80000, 2);")
conn.commit()

# Query to get employees in department 1
cursor.execute("""
    SELECT e.name, e.salary, d.name AS department 
    FROM Employee e 
    JOIN Department d ON e.departmentId = d.id 
    WHERE e.departmentId = 1;
""")
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)

# Use pandas to format the query result as a table
df = pd.read_sql_query("""
    SELECT e.name, e.salary, d.name AS department 
    FROM Employee e 
    JOIN Department d ON e.departmentId = d.id;
""", conn)
print(df)

conn.close()
