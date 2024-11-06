import sqlite3

# Function to connect to the database
def connect_db():
    return sqlite3.connect('company.db')

# Function to create tables
def create_tables(conn):
    cursor = conn.cursor()
    
    # Create employees table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        salary REAL NOT NULL
    )
    ''')
    
    # Create departments table with foreign key to employees
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS departments (
        dept_id INTEGER PRIMARY KEY,
        dept_name TEXT NOT NULL,
        employee_id INTEGER,
        FOREIGN KEY (employee_id) REFERENCES employees(id)
    )
    ''')
    conn.commit()

# Function to insert employee data
def insert_employees(conn):
    cursor = conn.cursor()
    
    # Insert multiple employees
    cursor.execute("INSERT INTO employees (name, salary) VALUES ('John', 50000)")
    cursor.execute("INSERT INTO employees (name, salary) VALUES ('Jane', 60000)")
    cursor.execute("INSERT INTO employees (name, salary) VALUES ('Mike', 55000)")
    
    conn.commit()

# Function to insert departments data
def insert_departments(conn):
    cursor = conn.cursor()

    # Insert departments and link to employees
    cursor.execute("INSERT INTO departments (dept_name, employee_id) VALUES ('HR', 1)")
    cursor.execute("INSERT INTO departments (dept_name, employee_id) VALUES ('Finance', 2)")
    cursor.execute("INSERT INTO departments (dept_name, employee_id) VALUES ('IT', 3)")
    
    conn.commit()

# Function to fetch all employees
def fetch_employees(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    
    print("\nAll Employees:")
    for row in rows:
        print(row)

# Function to update employee salary
def update_salary(conn, name, new_salary):
    cursor = conn.cursor()
    cursor.execute("UPDATE employees SET salary = ? WHERE name = ?", (new_salary, name))
    conn.commit()

# Function to delete an employee by name
def delete_employee(conn, name):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM employees WHERE name = ?", (name,))
    conn.commit()

# Function to join employees and departments and fetch data
def fetch_employee_departments(conn):
    cursor = conn.cursor()
    cursor.execute('''
    SELECT employees.name, departments.dept_name 
    FROM employees 
    JOIN departments ON employees.id = departments.employee_id
    ''')
    rows = cursor.fetchall()
    
    print("\nEmployees and their Departments:")
    for row in rows:
        print(f"Employee: {row[0]}, Department: {row[1]}")

# Main program to demonstrate all operations
def main():
    # Step 1: Connect to the database
    conn = connect_db()

    # Step 2: Create tables
    create_tables(conn)

    # Step 3: Insert employee data
    insert_employees(conn)

    # Step 4: Insert departments data
    insert_departments(conn)

    # Step 5: Fetch and display all employees
    fetch_employees(conn)

    # Step 6: Update salary of Mike
    update_salary(conn, 'Mike', 58000)
    print("\nAfter updating Mike's salary:")
    fetch_employees(conn)

    # Step 7: Delete John from employees
    delete_employee(conn, 'John')
    print("\nAfter deleting John:")
    fetch_employees(conn)

    # Step 8: Fetch and display employees and their departments
    fetch_employee_departments(conn)

    # Step 9: Close the database connection
    conn.close()

if __name__ == '__main__':
    main()
