import sqlite3
conn=sqlite3.connect('data.db')
print("Opened database successfully")
conn.execute("INSERT INTO BANKS (ID, NAME, AGE, ADDRESS, SALARY) VALUES (12, 'GHANSHYAM', 25, 'CHENNAI', 15000.00)")
conn.execute("INSERT INTO BANKS (ID, NAME, AGE, ADDRESS, SALARY) VALUES (13, 'SHYAM', 23, 'MADRAS', 20000.00)")
conn.execute("INSERT INTO BANKS (ID, NAME, AGE, ADDRESS, SALARY) VALUES (14, 'SHAMLAL', 25, 'KOLKATA', 65000.00)")
conn.commit()
print("Records created successfully")
data=conn.execute("SELECT * FROM BANKS")
for row in data:
    print("ID = ",row[0])
    print("NAME = ",row[1])
    print("ADDRESS = ",row[2])
    print("SALARY = ",row[3],"\n")
conn.close()
