import tkinter as tk

class Administrator:
    def __init__(self, administrator_id, administrator_phone_number, new_project, administrator_email, employee_id, employee_first_name, employee_last_name, employee_phone_number, employee_email):
        self.administrator_id = administrator_id
        self.administrator_phone_number = administrator_phone_number
        self.new_project = new_project
        self.administrator_email = administrator_email
        self.employee_id = employee_id
        self.employee_first_name = employee_first_name
        self.employee_last_name = employee_last_name
        self.employee_phone_number = employee_phone_number
        self.employee_email = employee_email

assigned_projects_list = []

def show_assigned_projects():
    assigned_projects_window = tk.Toplevel(root)
    assigned_projects_window.title("Assigned Projects")

    assigned_projects_text = tk.Text(assigned_projects_window)
    assigned_projects_text.pack()

    for project in assigned_projects_list:
        project_info = f"""Administrator ID: {project.administrator_id}
Administrator Phone Number: {project.administrator_phone_number}
New Project: {project.new_project}
Administrator Email: {project.administrator_email}
Employee ID: {project.employee_id}
Employee First Name: {project.employee_first_name}
Employee Last Name: {project.employee_last_name}
Employee Phone Number: {project.employee_phone_number}
Employee Email: {project.employee_email}\n\n"""
        assigned_projects_text.insert(tk.END, project_info)

root = tk.Tk()
root.title("Assign Project")

id_label = tk.Label(root, text="ID:")
id_label.pack()
id_entry = tk.Entry(root)
id_entry.pack()

administrator_phone_number_label = tk.Label(root, text="Administrator Phone Number:")
administrator_phone_number_label.pack()
administrator_phone_number_entry = tk.Entry(root)
administrator_phone_number_entry.pack()

new_project_label = tk.Label(root, text="New Project:")
new_project_label.pack()
new_project_entry = tk.Entry(root)
new_project_entry.pack()

administrator_email_label = tk.Label(root, text="Administrator Email:")
administrator_email_label.pack()
administrator_email_entry = tk.Entry(root)
administrator_email_entry.pack()

employee_id_label = tk.Label(root, text="Employee ID:")
employee_id_label.pack()
employee_id_entry = tk.Entry(root)
employee_id_entry.pack()

employee_first_name_label = tk.Label(root, text="Employee First Name:")
employee_first_name_label.pack()
employee_first_name_entry = tk.Entry(root)
employee_first_name_entry.pack()

employee_last_name_label = tk.Label(root, text="Employee Last Name:")
employee_last_name_label.pack()
employee_last_name_entry = tk.Entry(root)
employee_last_name_entry.pack()

employee_phone_number_label = tk.Label(root, text="Employee Phone Number:")
employee_phone_number_label.pack()
employee_phone_number_entry = tk.Entry(root)
employee_phone_number_entry.pack()

employee_email_label = tk.Label(root, text="Employee Email:")
employee_email_label.pack()
employee_email_entry = tk.Entry(root)
employee_email_entry.pack()

# Creating a Label widget for displaying the message
employee_text_label = tk.Label(root, text="")
employee_text_label.pack()

def assign_project(administrator, project):
    administrator.new_project = project
    assigned_projects_list.append(administrator)
    employee_text_label.config(text="Project assigned successfully!")

assign_button = tk.Button(root, text="Assign Project", command=lambda: assign_project(Administrator(id_entry.get(), administrator_phone_number_entry.get(), new_project_entry.get(), administrator_email_entry.get(), employee_id_entry.get(), employee_first_name_entry.get(), employee_last_name_entry.get(), employee_phone_number_entry.get(), employee_email_entry.get()), new_project_entry.get()))
assign_button.pack()

show_button = tk.Button(root, text="Show Assigned Projects", command=show_assigned_projects)
show_button.pack()

root.mainloop()