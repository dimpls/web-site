import psycopg2

def connect_to_bd():
    return psycopg2.connect(
        database="BlackDoor",
        user="postgres",
        password="admin123",
        host="localhost",
        port="5432"
    )


try:
    conn = connect_to_bd()
    with conn.cursor() as cursor:
        """
        select
        """
        #cursor.execute("""SELECT * FROM public."User" """)
        #rows = cursor.fetchall()
        #print(rows)

        """
        insert
        """
        #cursor.execute(
        #    """INSERT INTO public."User" (user_id, email, password, name, phone_number) VALUES(2, 'Alexander@gmail.com', 'Alexander123', 'Alexander', '71234567899')"""
        #)
        #conn.commit()

        """
        delete
        """
        #cursor.execute("""DELETE FROM public."User" WHERE user_id = 2 """)
        #conn.commit()

        """
        update
        """
        #cursor.execute("""UPDATE public."User" SET email = 'test' where user_id = 2""")
        #conn.commit()
except Exception as ex:
    print(ex)
finally:
    cursor.close()
