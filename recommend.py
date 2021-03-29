import psycopg2
import psycopg2.extras

#Moet nog ingevuld worden

DB_HOST= 'IP adress of the server where postgres is hosted on' 
DB_NAME= 'Name of the databse' 
DB_USER= 'user that you would connect with' 
DB_PASS= 'password that is used'

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)


cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

#Selecteer alle games uit database

cur.execute('SELECT * FROM iprop games; ')

print(cur.fetchall())

#Selecteer alle games met hetzelfde genre

cur.execute('SELECT * FROM iprop games, GROUP BY genre, HAVING count(*) > 1;')

print(cur.fetchall())

#Selecteer alle games met dezelfde rating

cur.execute('SELECT * FROM iprop games, GROUP BY rating, HAVING count(*) >1;')

print(cur.fetchall())

#Selecteer alle ratings van hoog naar laag

cur.execute('SELECT rating FROM iprop games, ORDER BY rating DESC;')

print(cur.fetchall())










conn.commit()
            
cur.close()

conn.close()



