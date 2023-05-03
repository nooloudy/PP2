import psycopg2

import random

connection = psycopg2.connect(
    host = "localhost",
    user = "postgres" ,
    password = "nooloudy",
    database = "postgres"
)
connection.autocommit = True
cursor = connection.cursor()

def createTable():
    cursor.execute('CREATE TABLE phone_book(id serial PRIMARY KEY,name varchar(100) NOT NULL,phone_number varchar(100) NOT NULL);')

cursor.execute(
   '''CREATE OR REPLACE PROCEDURE insert_data(nm VARCHAR, phon VARCHAR)
      LANGUAGE plpgsql
      AS $$
      DECLARE 
         cnt INTEGER;
      BEGIN
         SELECT INTO cnt (SELECT count(*) FROM phone_book WHERE name = nm);
         IF cnt > 0 THEN
            UPDATE phone_book
               SET phone_number = phon
               WHERE name = nm;
         ELSE
            INSERT INTO phone_book(name, phone_number) VALUES (nm, phon);
            END IF;
      END;
      $$;''')
cursor.execute(
    '''CREATE OR REPLACE FUNCTION search_from_bk(a VARCHAR, b VARCHAR)
      RETURNS SETOF phone_book 
   AS
   $$
      SELECT * FROM phone_book WHERE name = a AND phone_number = b;
   $$
   language sql;
   '''
)
cursor.execute(
   '''CREATE OR REPLACE PROCEDURE insert_to_book(nm VARCHAR, phon VARCHAR)
      LANGUAGE plpgsql
      AS $$
      DECLARE 
         cnt INTEGER;
      BEGIN
         SELECT INTO cnt (SELECT count(*) FROM phone_book WHERE name = nm);
         IF cnt > 0 THEN
            UPDATE phone_book
               SET phone_number = phon
               WHERE name = nm;
         ELSE
            INSERT INTO phone_book(name, phone_number) VALUES (nm, phon);
            END IF;
      END;
      $$;''')
cursor.execute(
    '''CREATE OR REPLACE FUNCTION paginating(a integer, b integer)
    RETURNS SETOF phone_book
    AS $$
    SELECT * FROM phone_book
	    ORDER BY name
	    LIMIT a OFFSET b;
    $$
    language sql;'''
)
cursor.execute(
   '''CREATE OR REPLACE PROCEDURE insert_list_data(
  IN users TEXT[][]
)
LANGUAGE plpgsql
AS $$
DECLARE
  i TEXT[];
BEGIN 
   Foreach i slice 1 in array users
   LOOP
      INSERT INTO phone_book (name, phone_number) VALUES (i[1], i[2]);
   END LOOP;
 
END
$$;
'''
)
run = False
while not run:
    a = input('Choose anything: \n\
            1.searching\n\
            2.insert\n\
            3.delete\n\
            4.paginating\n\
            5.insetloop\n\
            6.Exit\n\
                ')
    if a == '1':
        cursor.execute("SELECT search_data('Nurlybek' , '87072065547')")
        res = cursor.fetchall()
        print(res)
    if a == '2':
        cursor.execute("CALL insert_data('Muha Doskhan' ,'87772549885')")
    if a == '3':
        cursor.execute("CALL delete_data('Yuji Nishida')")
    if a == '4':
        cursor.execute('''SELECT * FROM paginating(5,2);''')
    if a == '5':
        cursor.execute('''CALL insert_list_data(ARRAY[
        ARRAY['Neymar JR', '87076052769'],
        ARRAY['Vini JR', '87079815569'],
        ARRAY['Raphinha', '87074793780']
        ]);''')  
    if a == '6':
        run = True
    connection.commit()

connection.close()
cursor.close()
