import sqlite3
from sqlite3 import Error
import employee

conn=sqlite3.connect(':memory:')
c=conn.cursor()

c.execute("""CREATE TABLE employees(
             employee_id integer,
             name text,
             phone text,
             age integer,
             role text 
             ) """)

def insert_emp(employee):
    with conn:
         c.execute("INSERT INTO employees VALUES (:employee_id, :name, :phone, :age, :role)",
                                        {'employee_id': employee.employee_id, 'name':employee.name, 'phone': employee.phone,'age': employee.age,'role': employee.role})

def get_emps_by_id(employee_id):
    c.execute("SELECT * FROM employees WHERE employee_id=:employee_id", {'employee_id': employee_id})
    return c.fetchall()

def get_emps_by_name(name):
    c.execute("SELECT * FROM employees WHERE name=:name", {'name': name})
    return c.fetchall()

def get_emps_by_phone(phone):
    c.execute("SELECT * FROM employees WHERE phone=:phone", {'phone': phone})
    return c.fetchall()

def get_emps_by_age(age):
    c.execute("SELECT * FROM employees WHERE age=:age", {'age': age})
    return c.fetchall()

def get_emps_by_role(role):
    c.execute("SELECT * FROM employees WHERE role=:role", {'role': role})
    return c.fetchall()

def update_name(employee,name):
    with conn:
        c.execute("""UPDATE employees SET name=:name
                     WHERE employee_id= :employee_id""",
                     {'employee_id': employee.employee_id, 'name': name, 'phone': employee.phone,'age': employee.age,'role': employee.role})        

def update_phone(employee,phone):
    with conn:
        c.execute("""UPDATE employees SET phone=:phone
                     WHERE employee_id= :employee_id""",
                     {'employee_id': employee.employee_id, 'name':employee.name, 'phone': phone,'age': employee.age,'role': employee.role})

def update_age(employee,age):
    with conn:
        c.execute("""UPDATE employees SET age=:age
                     WHERE employee_id= :employee_id""",
                     {'employee_id': employee.employee_id, 'name':employee.name, 'phone': employee.phone,'age': age,'role': employee.role})

def update_role(employee,role):
    with conn:
        c.execute("""UPDATE employees SET role=:role
                     WHERE employee_id= :employee_id""",
                     {'employee_id': employee.employee_id, 'name':employee.name, 'phone': employee.phone,'age': employee.age,'role': role})

def remove_emp(employee):
    with conn:
        c.execute("DELETE from employees where employee_id= :employee_id",
        {'employee_id': employee.employee_id})


def main():
employee_one = employee.Employee(
    "Jane",
    "555-456-0987",
    45,
    "junior"
    ) 

employee_two=employee.Manager(
    "Jane",
    "666-456-0123",
    56,
    "manager"
    ) 

employee_three = employee.Senior(
    "Bob",
    "777-456-0987",
    35,
    "senior"
    ) 

insert_emp(employee_one)
insert_emp(employee_two)
insert_emp(employee_three)
emps=get_emps_by_name('Jane')
print(emps)

update_phone(employee_two,"778-458-2589")
update_age(employee_two,40)
update_role(employee_two,"senior")
remove_emp(employee_one)
emps=get_emps_by_phone('777-456-0987')
print(emps)

update_name(employee_three,"Jim")
emps=get_emps_by_age("40")
print(emps)

conn.close()             