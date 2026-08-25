import tkinter
from tkinter import ttk
from tkinter import StringVar

def addcab():
    print("test")


root = tkinter.Tk()
root.title("CUTTING LIST GENERATOR")

main_frame = ttk.Frame(root, padding=(3, 3, 12, 12))
main_frame.grid(column=0,row=0)

input_frame = ttk.Frame(main_frame, padding=(3, 3, 12, 12))
input_frame.grid(column=0,row=0)

ttk.Label(input_frame,text="Type: ", anchor="w").grid(column=0,row=0)

cab_type= StringVar()
cmb_type= ttk.Combobox(input_frame,textvariable=cab_type)
cmb_type.grid(column=1,row=0)

ttk.Label(input_frame,text="Length: ", anchor="w").grid(column=0,row=1)

length = StringVar()
entry_len = ttk.Entry(input_frame,textvariable=length)
entry_len.grid(column=1,row=1)

btn_add = ttk.Button(input_frame, text= "Add", command= addcab)
btn_add.grid(column=2,row=3)

root.mainloop()


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