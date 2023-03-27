import psycopg2
from Employee import Employee
from Review import Review
from Session import Session
from Sketch import Sketch
from User import User



def connect_to_bd():
    return psycopg2.connect(
        database="BlackDoor",
        user="postgres",
        password="admin123",
        host="localhost",
        port="5432"
    )


def insertToBD(obj):
    try:
        conn = connect_to_bd()
        with conn.cursor() as cursor:
            if isinstance(obj, Employee):
                print("[INFO] Employee")
                query = """INSERT INTO public."Employee"(employee_id, name, email, password, phone_number, work_experience, position) VALUES(%s, %s, %s, %s, %s, %s, %s)"""
                values = tuple(vars(obj).values())
                cursor.execute(query, values)
            elif isinstance(obj, User):
                print("[INFO] User")
                query = """INSERT INTO public."User"(user_id, email, password, name, phone_number) VALUES(%s, %s, %s, %s, %s)"""
                values = tuple(vars(obj).values())
                cursor.execute(query, values)
            elif isinstance(obj, Session):
                print("[INFO] Session")
                query = """INSERT INTO public."Session"(session_id, user_id, date, description, status, employee_id, sketch_id) VALUES(%s, %s, %s, %s, %s, %s, %s)"""
                values = tuple(vars(obj).values())
                cursor.execute(query, values)
            elif isinstance(obj, Review):
                print("[INFO] Review")
                query = """INSERT INTO public."Review"(review_id, user_id, employee_id, body) VALUES(%s, %s, %s, %s)"""
                values = tuple(vars(obj).values())
                cursor.execute(query, values)
            elif isinstance(obj, Sketch):
                print("[INFO] Sketch")
                query = """INSERT INTO public."Sketch"(sketch_id, description, price) VALUES(%s, %s, %s)"""
                values = tuple(vars(obj).values())
                cursor.execute(query, values)
            conn.commit()
    except Exception as ex:
        print("[INFO]", ex)
    finally:
        conn.close()


def deleteFromBD(obj):
    try:
        conn = connect_to_bd()
        with conn.cursor() as cursor:
            if isinstance(obj, Employee):
                print("[INFO] Employee")
                query = f"""DELETE FROM public."Employee" WHERE employee_id =  """ + str(list(vars(obj).values())[0])
                cursor.execute(query)
            elif isinstance(obj, User):
                print("[INFO] User")
                query = """DELETE FROM public."User" WHERE user_id =  """ + str(list(vars(obj).values())[0])
                cursor.execute(query)
            elif isinstance(obj, Session):
                print("[INFO] Session")
                query = """DELETE FROM public."Session" WHERE session_id =  """ + str(list(vars(obj).values())[0])
                cursor.execute(query)
            elif isinstance(obj, Review):
                print("[INFO] Review")
                query = """DELETE FROM public."Review" WHERE review_id =  """ + str(list(vars(obj).values())[0])
                cursor.execute(query)
            elif isinstance(obj, Sketch):
                print("[INFO] Sketch")
                query = """DELETE FROM public."Sketch" WHERE sketch_id =  """ + str(list(vars(obj).values())[0])
                cursor.execute(query)
            conn.commit()
    except Exception as ex:
        print(ex)
    finally:
        conn.close()


def updateInBd(obj, column_name, new_value):
    try:
        conn = connect_to_bd()
        with conn.cursor() as cursor:
            if isinstance(obj, Employee):
                print("[INFO] Employee")
                query = f"""UPDATE public."Employee" SET {str(column_name)} = '{str(new_value)}' where employee_id = {str(list(vars(obj).values())[0])}"""
                cursor.execute(query)
            elif isinstance(obj, User):
                print("[INFO] User")
                query = f"""UPDATE public."User" SET {str(column_name)} = '{str(new_value)}' where user_id = {str(list(vars(obj).values())[0])}"""
                cursor.execute(query)
            elif isinstance(obj, Session):
                print("[INFO] Session")
                query = f"""UPDATE public."Session" SET {str(column_name)} = '{str(new_value)}' where session_id = {str(list(vars(obj).values())[0])}"""
                cursor.execute(query)
            elif isinstance(obj, Review):
                print("[INFO] Review")
                query = f"""UPDATE public."Review" SET {str(column_name)} = '{str(new_value)}' where review_id = {str(list(vars(obj).values())[0])}"""
                cursor.execute(query)
            elif isinstance(obj, Sketch):
                print("[INFO] Sketch")
                query = f"""UPDATE public."Sketch" SET {str(column_name)} = '{str(new_value)}' where sketch_id = {str(list(vars(obj).values())[0])}"""
                cursor.execute(query)
            conn.commit()
    except Exception as ex:
        print(ex)
    finally:
        conn.close()


emp = Employee(1, 'ИмяФам', 'email@gmail.com', 'password123', '79371112312', 2, 'Master')
usr = User(2, 'email@gmail.com', 'password123', 'ИмяФам', '79371112312')
sess = Session(1, 3, '12.03.2023', 'Дракона хочу', 'В процессе', 2, 1)
rew = Review(1, 2, 2, '10/10')
skt = Sketch(1, 'Dog', 1322)
#insertToBD(skt)
#deleteFromBD(skt)
#updateInBd(skt, 'price', '2555')
