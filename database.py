import sqlite3

def create_connection(db_file):
    """ create a database connection to the SQLite database specified by db_file """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to {db_file} successfully")
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

def add_student(student):
    """ Add a new student to the students table """
    conn = sqlite3.connect("student_management_system.db")
    with conn:
        sql = ''' INSERT INTO students(name, age, course, contact)
                  VALUES(?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, student)
        conn.commit()
        return cur.lastrowid

def view_students(sort_by=None):
    """ View all students in the students table """
    conn = sqlite3.connect("student_management_system.db")
    cur = conn.cursor()
    query = "SELECT * FROM students"
    if sort_by != None:
        query += f" ORDER BY {sort_by}"
    cur.execute(query)
    rows = cur.fetchall()
    return rows


def update_student(student):
    """ Update a student in the students table """
    conn = sqlite3.connect("student_management_system.db")
    sql = ''' UPDATE students
              SET name = ?,
                  age = ?,
                  course = ?,
                  contact = ?
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, student)
    conn.commit()

def delete_student(id):
    """ Delete a student by student id """
    conn = sqlite3.connect("student_management_system.db")
    sql = 'DELETE FROM students WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()

def search_student(keyword):
    """ Search for a student by name, course, or contact """
    conn = sqlite3.connect("student_management_system.db")
    cur = conn.cursor()
    query = "SELECT * FROM students WHERE name LIKE ? OR course LIKE ? OR contact LIKE ?"
    cur.execute(query, ('%'+keyword+'%', '%'+keyword+'%', '%'+keyword+'%'))
    rows = cur.fetchall()
    for row in rows:
        print(row)

def main():
    database = "student_management_system.db"

    sql_create_students_table = """ CREATE TABLE IF NOT EXISTS students (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        name TEXT NOT NULL,
                                        age INTEGER NOT NULL,
                                        course TEXT NOT NULL,
                                        contact TEXT NOT NULL
                                    ); """

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create students table
        create_table(conn, sql_create_students_table)
    else:
        print("Error! cannot create the database connection.")

#     # Example usage
#     with conn:
#         # Add a new student
#         student = ('John Doe', 20, 'Computer Science', '1234567890')
#         student_id = add_student(conn, student)

#         # View students
#         print("All students:")
#         view_students(conn)

#         # Update student
#         updated_student = ('John Doe', 21, 'Computer Science', '0987654321', student_id)
#         update_student(conn, updated_student)

#         # View students sorted by name
#         print("Students sorted by name:")
#         view_students(conn, sort_by='name')

#         # Search student
#         print("Search results for 'John':")
#         search_student(conn, 'John')

#         # Delete student
#         delete_student(conn, student_id)

# if __name__ == '__main__':
#     main()
