import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='user', password='password',db='mydb')
conn.autocommit(True)
cursor = conn.cursor()
insert_query = """
    INSERT INTO mydb.dogs (name, age, breed)
    VALUES (%s, %s, %s)
    """
values_to_insert = [
    ('Roni', 1, 'German Shepherd'),
    ('Moni', 2, 'Boxer'),
    ('Toni', 3, 'PitBull')
]

cursor.executemany(insert_query, values_to_insert)

update_query = """
    UPDATE mydb.dogs
    SET age = 4
    WHERE breed = %s
    """
breed_to_update = 'Boxer'
cursor.execute(update_query, (breed_to_update,))

delete_query = """
    DELETE FROM mydb.dogs
    WHERE breed = %s
    """
breed_to_delete = 'PitBull'
cursor.execute(delete_query, (breed_to_delete,))

cursor.execute('Select * from mydb.dogs')

for row in cursor:
    print(row)

cursor.close()
conn.close()