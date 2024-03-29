import tkinter as tk

class Project:
    def __init__(self, projectid, projectname, material, duration, additionalcost):
        self.projectid = projectid
        self.projectname = projectname
        self.material = material
        self.assignedemployee = None
        self.duration = duration
        self.additionalcost = additionalcost

project_list = []  # Create an empty list to store projects

def create_project():
    projectid = projectid_entry.get()
    projectname = projectname_entry.get()
    material = material_entry.get()
    duration = duration_entry.get()
    additionalcost = additionalcost_entry.get()

    new_project = Project(projectid, projectname, material, duration, additionalcost)
    project_list.append(new_project)
    result_label.config(text="Project Created")

def display_projects():
    project_text = ""
    for project in project_list:
        project_text += f"Project ID: {project.projectid}, Project Name: {project.projectname}, Material: {project.material}, Duration: {project.duration}, Additional Cost: {project.additionalcost}\n"
    project_text_label.config(text=project_text)

# Create the GUI
root = tk.Tk()
root.title("Create Project")

# Labels and Entry fields
projectid_label = tk.Label(root, text="Project ID:")
projectid_label.pack()
projectid_entry = tk.Entry(root)
projectid_entry.pack()

projectname_label = tk.Label(root, text="Project Name:")
projectname_label.pack()
projectname_entry = tk.Entry(root)
projectname_entry.pack()

material_label = tk.Label(root, text="Material:")
material_label.pack()
material_entry = tk.Entry(root)
material_entry.pack()

duration_label = tk.Label(root, text="Duration:")
duration_label.pack()
duration_entry = tk.Entry(root)
duration_entry.pack()

additionalcost_label = tk.Label(root, text="Additional Cost:")
additionalcost_label.pack()
additionalcost_entry = tk.Entry(root)
additionalcost_entry.pack()

# Button to create project
create_button = tk.Button(root, text="Create Project", command=create_project)
create_button.pack()

# Button to display projects
display_button = tk.Button(root, text="Projects List", command=display_projects)
display_button.pack()

# Label to display result
result_label = tk.Label(root, text="")
result_label.pack()

# Label to display project list
project_text_label = tk.Label(root, text="")
project_text_label.pack()

root.mainloop()