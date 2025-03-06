# Employee Class (including all Employee functionalities)
class Employee:
    def __init__(self, emp_id, name, position, salary):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary
        self.projects = []

    def update_info(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def assign_project(self, project_id):
        self.projects.append(project_id)

    def remove_project(self, project_id):
        if project_id in self.projects:
            self.projects.remove(project_id)

    def get_details(self):
        return {
            "ID": self.emp_id,
            "Name": self.name,
            "Position": self.position,
            "Salary": self.salary,
            "Projects": self.projects,
        }

    def __str__(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Position: {self.position}, Salary: {self.salary}, Projects: {self.projects}"

# Department Class to add Employees and Managers as well
class Department:
    def __init__(self, department_id, name):
        self.department_id = department_id
        self.name = name
        self.manager_id = None
        self.employees = []

    def assign_manager(self, manager_id):
        self.manager_id = manager_id

    def add_employee(self, emp_id):
        if emp_id not in self.employees:
            self.employees.append(emp_id)

    def remove_employee(self, emp_id):
        if emp_id in self.employees:
            self.employees.remove(emp_id)

    def get_department_details(self):
        return {
            "ID": self.department_id,
            "Name": self.name,
            "Manager": self.manager_id,
            "Employees": self.employees,
        }

    def __str__(self):
        return f"ID: {self.department_id}, Name: {self.name}, Manager: {self.manager_id}, Employees: {self.employees}"

# Project Class to manage projects and employee assignments
class Project:
    def __init__(self, project_id, name, budget, deadline):
        self.project_id = project_id
        self.name = name
        self.budget = budget
        self.deadline = deadline
        self.employees = []

    def assign_employee(self, emp_id):
        if emp_id not in self.employees:
            self.employees.append(emp_id)

    def remove_employee(self, emp_id):
        if emp_id in self.employees:
            self.employees.remove(emp_id)

    def update_budget(self, budget):
        self.budget = budget

    def update_deadline(self, deadline):
        self.deadline = deadline

    def get_project_details(self):
        return {
            "ID": self.project_id,
            "Name": self.name,
            "Budget": self.budget,
            "Deadline": self.deadline,
            "Employees": self.employees,
        }

    def __str__(self):
        return f"ID: {self.project_id}, Name: {self.name}, Budget: {self.budget}, Deadline: {self.deadline}, Employees: {self.employees}"

# HRSystem Class to manage employees, departments, and projects
class HRSystem:
    def __init__(self):
        self.employees = []
        self.departments = []
        self.projects = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def add_department(self, department):
        self.departments.append(department)

    def add_project(self, project):
        self.projects.append(project)

#----------------------------------------Main--------------------------------

hr = HRSystem()


emp1 = Employee(1, "Ali", "Software Engineer", 15000)
emp2 = Employee(2, "Mona", "Data Scientist", 18000)
emp3 = Employee(3, "Kareem", "Project Manager", 25000)


hr.add_employee(emp1)
hr.add_employee(emp2)
hr.add_employee(emp3)


dept1 = Department(101, "Engineering")
dept2 = Department(102, "Data Science")


hr.add_department(dept1)
hr.add_department(dept2)


dept1.assign_manager(emp1.emp_id)
dept2.assign_manager(emp2.emp_id)


dept1.add_employee(emp1.emp_id)
dept1.add_employee(emp3.emp_id)
dept2.add_employee(emp2.emp_id)


proj1 = Project(201, "AI Chatbot", 50000, "30-Apr-2025")
proj2 = Project(202, "E-commerce Platform", 75000, "15-May-2025")


hr.add_project(proj1)
hr.add_project(proj2)


proj1.assign_employee(emp1.emp_id)
proj1.assign_employee(emp2.emp_id)
proj2.assign_employee(emp3.emp_id)


emp1.assign_project(proj1.project_id)
emp2.assign_project(proj1.project_id)
emp3.assign_project(proj2.project_id)


print("\n--- Employees ---")
for employee in hr.employees:
    print(employee)

print("\n--- Departments ---")
for department in hr.departments:
    print(department)

print("\n--- Projects ---")
for project in hr.projects:
    print(project)





