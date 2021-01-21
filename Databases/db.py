import psycopg2

# Establish connection to database
con = psycopg2.connect(
            host='localhost',
            database='psyco',
            user='postgres',
            password='mario2',
            port=5433
)

# cursor
cur = con.cursor()

# Execute Query
cur.execute("INSERT INTO employees (id, name) VALUES (%s, %s)", (1, "Hussein") )
cur.execute("select id, name from employees")

rows = cur.fetchall()  # array of tuples such as [(id, name)]
for r in rows:
    print(f"id {r[0]} name {r[1]}")

# Commit changes
con.commit()

# Close the cursor. LEAKING IS THE WORST.
cur.close()

# Close the connection
con.close()
