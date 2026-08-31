import tkinter
from tkinter import messagebox
from tkinter import ttk
from tkinter import StringVar
from tkinter import simpledialog
import carpent


def btn_add_clicked():
    add_type = cab_type.get()
    if len(add_type) == 0:
        messagebox.showerror("Info", "Please select type")
        return

    try:
        add_length = int(length.get())
    except ValueError:
        messagebox.showerror("Error", "Please input number into length!")
        return

    if add_length < 99:
        messagebox.showerror("Info", "Can not be less than 99 mm")
        return

    carpent.gui_order(project, add_type, add_length)
    length.set("")

    item_id = tree.insert("", "end", text="", values=[add_type, add_length])

    # project_list is a dict usind the itemid as the key
    # and the actual cabinet is inserted
    project_list[item_id] = project[-1]


def btn_remove_clicked():
    selected_item = tree.selection()

    for item_id in selected_item:
        cabinet = project_list[item_id]

        del project_list[item_id]
        project.remove(cabinet)
        tree.delete(item_id)


def btn_create_clicked():
    if len(project) < 1:
        return
    project_name = simpledialog.askstring("Project Name", "Enter Project Name")
    if messagebox.askquestion(
        "Project Confermation", f"Do you want to create project named: {project_name}"
    ):
        if carpent.gui_output(project, project_name) == False:
            messagebox.showerror(
                "Error",
                "Error while creating file\n File my be openned by another app!",
            )


root = tkinter.Tk()
root.title("CUTTING LIST GENERATOR")

project = list()
project_list = dict()

main_frame = ttk.Frame(root, padding=(3, 3, 12, 12))
main_frame.grid(column=0, row=0)

input_frame = ttk.Frame(main_frame, padding=(3, 3, 12, 12))
input_frame.grid(column=0, row=0)

ttk.Label(input_frame, text="Type: ", anchor="w").grid(column=0, row=0)

cab_type = StringVar()
cmb_type = ttk.Combobox(input_frame, textvariable=cab_type)
cmb_type.grid(column=1, row=0)
cmb_type["values"] = ["Bottom", "Wall"]
cmb_type.state(["readonly"])

ttk.Label(input_frame, text="Length: ", anchor="w").grid(column=0, row=1)

length = StringVar()
entry_len = ttk.Entry(input_frame, textvariable=length)
entry_len.grid(column=1, row=1)

btn_add = ttk.Button(input_frame, text="Add", command=btn_add_clicked, default="active")
btn_add.grid(column=1, row=3)

show_frame = ttk.Frame(main_frame, padding=(3, 3, 12, 12))
show_frame.grid(column=0, row=1)

tree = ttk.Treeview(show_frame, height=5, columns=["type", "length"], show="headings")
tree.grid(column=0, row=0)
tree.heading("type", text="Type")
tree.heading("length", text="Length")
tree.column("type", anchor="center")
tree.column("length", anchor="center")

tree_scrollbar = ttk.Scrollbar(show_frame,orient='vertical', command=tree.yview)
tree.configure(yscrollcommand=tree_scrollbar.set)
tree_scrollbar.grid(column=1,row=0, sticky= ('n','s'))

btn_remove = ttk.Button(show_frame, text="Remove", command=btn_remove_clicked)
btn_remove.grid(column=0, row=1)

btn_create = ttk.Button(main_frame, text="Create Excel", command=btn_create_clicked)
btn_create.grid(column=0, row=2)

root.resizable(False, False)
root.mainloop()


# concept created by Claude
# ┌──────────────────────────────────────────────┐
# │              Cabinet Project                 │
# ├──────────────────────────────────────────────┤
# │ Type:    [ Cabinet ▼ ]                       │
# │ Length:  [ 600       ] mm                    │
# │                                              │
# │             [ Add Cabinet ]                  │
# ├──────────────────────────────────────────────┤
# │ Cabinets                                     │
# │                                              │
# │  #     Type          Length                  │
# │ ──────────────────────────────────────────── │
# │  1     Cabinet       600 mm                  │
# │  2     Wall          800 mm                  │
# │  3     Cabinet       450 mm                  │
# │                                              │
# ├──────────────────────────────────────────────┤
# │ [ Remove Selected ]                          │
# │                                              │
# │              [ Create Excel ]                │
# └──────────────────────────────────────────────┘
