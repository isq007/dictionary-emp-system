employees = {
   "E101": {"name": "Alice Johnson", "age": 30, "department": "HR"},
   "E102": {"name": "Bob Smith", "age": 25, "department": "IT"}
}
import random

def generate_employee_id():
    return "E" + str(random.randint(100, 999))
def add_employee():
    """Adds a new employee with data validation."""
    emp_id = generate_employee_id()
    while emp_id in employees:  # Ensure unique ID
        emp_id = generate_employee_id()

    name = input("Enter Name: ").strip()
    if not name.replace(" ", "").isalpha():
        print("Invalid name! Name should contain only letters.")
        return

    try:
        age = int(input("Enter Age: "))
        if age <= 0:
            print("Invalid age! Age must be a positive integer.")
            return
    except ValueError:
        print("Invalid age! Age must be a number.")
        return

    department = input("Enter Department: ").strip()

    employees[emp_id] = {"name": name, "age": age, "department": department}
    print(f"Employee {emp_id} added successfully!")
def remove_employee():
    """Removes an employee by ID."""
    emp_id = input("Enter Employee ID to remove: ").strip()
    if emp_id in employees:
        del employees[emp_id]
        print(f"Employee {emp_id} removed successfully!")
    else:
        print("Employee ID not found!")
def update_employee():
    """Updates an employee's details."""
    emp_id = input("Enter Employee ID to update: ").strip()
    if emp_id not in employees:
        print("Employee ID not found!")
        return

    print("Leave blank to keep existing values.")

    new_name = input("Enter New Name: ").strip()
    if new_name and not new_name.replace(" ", "").isalpha():
        print("Invalid name!")
        return

    new_age = input("Enter New Age: ").strip()
    if new_age:
        try:
            new_age = int(new_age)
            if new_age <= 0:
                print("Invalid age!")
                return
        except ValueError:
            print("Invalid age!")
            return

    new_department = input("Enter New Department: ").strip()

    if new_name:
        employees[emp_id]["name"] = new_name
    if new_age:
        employees[emp_id]["age"] = new_age
    if new_department:
        employees[emp_id]["department"] = new_department

    print(f"Employee {emp_id} updated successfully!")
def search_employee():
    """Search employees by ID or Name."""
    search_term = input("Enter Employee ID or Name: ").strip().lower()
    
    found = False
    for emp_id, details in employees.items():
        if emp_id.lower() == search_term or details["name"].lower() == search_term:
            print(f"ID: {emp_id}, Name: {details['name']}, Age: {details['age']}, Department: {details['department']}")
            found = True
    if not found:
        print("Employee not found!")
def sort_employees():
    """Sort employees by Name, Age, or Department."""
    print("Sort by: 1. Name  2. Age  3. Department")
    choice = input("Enter choice: ").strip()

    if choice == "1":
        sorted_list = sorted(employees.items(), key=lambda x: x[1]["name"])
    elif choice == "2":
        sorted_list = sorted(employees.items(), key=lambda x: x[1]["age"])
    elif choice == "3":
        sorted_list = sorted(employees.items(), key=lambda x: x[1]["department"])
    else:
        print("Invalid choice!")
        return

    for emp_id, details in sorted_list:
        print(f"ID: {emp_id}, Name: {details['name']}, Age: {details['age']}, Department: {details['department']}")
def main():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. Update Employee")
        print("4. Search Employee")
        print("5. Sort Employees")
        print("6. Exit")
        
        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_employee()
        elif choice == "2":
            remove_employee()
        elif choice == "3":
            update_employee()
        elif choice == "4":
            search_employee()
        elif choice == "5":
            sort_employees()
        elif choice == "6":
            print("Exiting Employee Management System. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1-6.")
if __name__ == "__main__":
    main()
# Solution
