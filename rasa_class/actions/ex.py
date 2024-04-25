# import sqlite3


# conn = sqlite3.connect('final.db')

# class course:
#     def create_course_database():
#         w = conn.cursor()

#         w.execute(""" CREATE TABLE core (
#                   ncourse text ,
#                   description text
                
#         )""" )


#         w.execute("INSERT INTO  core VALUES('os','opriting')")
#         w.execute("SELECT * FROM core WHERE ncourse ='Math'")

#         print(w.fetchall())

#         conn.commit()
#     def select(self,course_name):

#         w = conn.cursor()

#         w.execute('''
#           SELECT * FROM core WHERE ncourse = ?;
#              ''', (course_name,))
#         rows = w.fetchall()
#         query_result = [('CourseDescription',rows), ('AnotherDescription',rows)]  

#         return query_result

#         return rows
#         conn.commit()