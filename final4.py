import sqlite3
import cv2
import glob
from pyzbar.pyzbar import decode
import _pickle as pickle

def decode_qr_code(image_path):
    try:
        img = cv2.imread(image_path)
        decoded_objects = decode(img)
    except Exception as e:
        print(f"the error was {e}")
        return None
    else:
        return decoded_objects[0].data.decode("utf-8")
    
def word_segmentaion(pers, types):
    a_list_string = pers.split()
    a_list_field = list()
    for i in range( a_list_string.__len__()):
        funct = types[i]
        field = funct(a_list_string[i]) 
        a_list_field.append(field)
    return tuple( a_list_field)
    
def DB_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except Exception as e:
        print(f"the error was {e}")
    return conn
    
def insert_task(cur, query, data):
    try:
        cur.executemany(query, data)
    except Exception as e:
        print(e)

def select_tasks(cursor, query):
    try:
        cursor.execute(query)
    except Exception as e:
        print(f" The error was {e}")
        return None
    else:
        return cursor.fetchall()

files = glob.glob('images/*.png')
students = []
types = [str, str, str, str, str, str, float]

for file in files:
    person = decode_qr_code(file)
    students.append(word_segmentaion(person, types))

# for student in students:
#     print(student)

db = r"student.db"
conn = DB_connection(db)

with conn:
    cursor = conn.cursor()
    query = '''
    CREATE TABLE IF NOT EXISTS Female (
        student_id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        faculty TEXT NOT NULL,
        department TEXT NOT NULL,
        phone TEXT NOT NULL,
        gpa REAL NOT NULL
    );
    '''
    cursor.execute(query)
    query = '''
    CREATE TABLE IF NOT EXISTS Male (
        student_id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        faculty TEXT NOT NULL,
        department TEXT NOT NULL,
        phone TEXT NOT NULL,
        gpa REAL NOT NULL
    );
    '''
    cursor.execute(query)

females = []
males = []

with conn:
    cursor = conn.cursor()
    for student in students:
        if student[2] == 'F':
            s = list(student)
            s.pop(2)
            females.append(tuple(s))
        elif student[2] == 'M':
            s = list(student)
            s.pop(2)
            males.append(tuple(s))            
        else:
            print(f"warning: sex incorrect {student}")

with conn:
    cursor = conn.cursor()
    query = 'INSERT INTO Female (student_id, name, faculty, department, phone, gpa )  VALUES (?,?,?,?,?,?)'
    insert_task(cursor, query, females)
    query = 'INSERT INTO Male (student_id, name, faculty, department, phone, gpa )  VALUES (?,?,?,?,?,?)'
    insert_task(cursor, query, males)
    conn.commit()


# binary file
class Student(object):
    def __init__(self,std_id, name, faculty, department, phone, gpa):
        self.student_id = std_id
        self.name = name
        self.faculty = faculty
        self.department = department
        self.phone = phone
        self.gpa = gpa

class Student(object):
    def __init__(self, record, sex):
        self.student_id = record[0]
        self.name = record[1]
        self.faculty = record[2]
        self.department = record[3]
        self.phone = record[4]
        self.gpa = record[5]
        self.sex = sex
    def __str__(self):
        return f"({self.student_id} {self.name} {self.faculty} {self.department} {self.phone} {self.gpa} {self.sex})"
    
with conn:
    cursor = conn.cursor()
    a_list_object = list()

    query = 'SELECT * from Female'; 
    rows = select_tasks(cursor, query)
    for record in rows:
        emp = Student(record, 'F')
        a_list_object.append(emp)


    query = 'SELECT * from Male'; 
    rows = select_tasks(cursor, query)
    for record in rows:
        emp = Student(record, 'M')
        a_list_object.append(emp)

    with open("./outs/Object_records.bin", "wb") as file:
        try:
            pickle.dump(a_list_object, file)
        except Exception as e:
            print(e)
        else:
            print('dump complete')

try:
    with open('./outs/Object_records.bin', 'rb') as file:
        data = pickle.load(file)
except Exception as e:
    print(f"error is {e}        {e.__class__}")
else:
    for obj in data:
        print(obj)

print('---final---')
female_gpa_upper_3 = []
female_gpa_lower_3 = []
male_gpa_upper_3 = []
male_gpa_lower_3 = []
try:
    with open('./outs/Object_records.bin', 'rb') as file:
        data = pickle.load(file)
except Exception as e:
    print(f"error is {e}        {e.__class__}")
else:
    for obj in data:
        if obj.sex == 'F':
            if obj.gpa > 3.0:
                female_gpa_upper_3.append(obj)
            else:
                female_gpa_lower_3.append(obj)
        else:
            if obj.gpa > 3.0:
                male_gpa_upper_3.append(obj)
            else:
                male_gpa_lower_3.append(obj)
    print(f'number of female has gpa upper 3 : {len(female_gpa_upper_3)} people')
    for obj in female_gpa_upper_3:
        print(f'\t{obj}')
    print(f'number of female has gpa lower 3 : {len(female_gpa_lower_3)} people')
    for obj in female_gpa_lower_3:
        print(f'\t{obj}')
    print(f'number of male has gpa upper 3 : {len(male_gpa_upper_3)} people')
    for obj in male_gpa_upper_3:
        print(f'\t{obj}')
    print(f'number of male has gpa lower 3 : {len(male_gpa_lower_3)} people')
    for obj in male_gpa_lower_3:
        print(f'\t{obj}')