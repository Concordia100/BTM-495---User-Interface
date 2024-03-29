import tkinter as tk

class Employee:
    def __init__(self, role, employee_id, password, phonenum, email, availability, first_name, last_name):
        self.role = role
        self.project = None
        self.employee_id = employee_id
        self.password = password
        self.phonenum = phonenum
        self.email = email
        self.availability = availability
        self.first_name = first_name
        self.last_name = last_name

employee_list = []

def create_employee():
    role = role_entry.get()
    employee_id = id_entry.get()
    password = password_entry.get()
    phonenum = phonenum_entry.get()
    email = email_entry.get()
    availability = availability_entry.get()
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()

    new_employee = Employee(role, employee_id, password, phonenum, email, availability, first_name, last_name)
    employee_list.append(new_employee)
    result_label.config(text="Employee Created")

def display_employees():
    employee_text = ""
    for employee in employee_list:
        employee_text += f"Role: {employee.role}, Employee ID: {employee.employee_id}, Password: {employee.password}, Phone Number: {employee.phonenum}, Email: {employee.email}, Availability: {employee.availability}, First Name: {employee.first_name}, Last Name: {employee.last_name}\n"
    employee_text_label.config(text=employee_text)

# Create the GUI
root = tk.Tk()
root.title("Create Employee")

# Labels and Entry fields
first_name_label = tk.Label(root, text="First Name:")
first_name_label.pack()
first_name_entry = tk.Entry(root)
first_name_entry.pack()

last_name_label = tk.Label(root, text="Last Name:")
last_name_label.pack()
last_name_entry = tk.Entry(root)
last_name_entry.pack()

id_label = tk.Label(root, text="Employee ID:")
id_label.pack()
id_entry = tk.Entry(root)
id_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root)
password_entry.pack()

phonenum_label = tk.Label(root, text="Phone Number:")
phonenum_label.pack()
phonenum_entry = tk.Entry(root)
phonenum_entry.pack()

email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

availability_label = tk.Label(root, text="Availability:")
availability_label.pack()
availability_entry = tk.Entry(root)
availability_entry.pack()

role_label = tk.Label(root, text="Role:")
role_label.pack()
role_entry = tk.Entry(root)
role_entry.pack()

# Button to create employee
create_button = tk.Button(root, text="Create Employee", command=create_employee)
create_button.pack()

# Button to display employees
display_button = tk.Button(root, text="Employees List", command=display_employees)
display_button.pack()

# Label to display result
result_label = tk.Label(root, text="")
result_label.pack()

# Label to display employee list
employee_text_label = tk.Label(root, text="")
employee_text_label.pack()

root.mainloop()
