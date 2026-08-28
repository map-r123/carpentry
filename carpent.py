# The cabinet class is an object that returns all the componets that make a cabinet excluding the top
# each function returns a dict with information about that particular panal
from openpyxl import Workbook
import time


class Cabinet:
    def __init__(self, length, width=600, height=740):
        self.length = length
        self.width = width - 30
        self.height = height

    def bottom(self):
        # length is how wide the cabinet is and width is how deep the cabinet is
        return {
            "name": "bottom_panel",
            "Edge": "front",
            "length": f"{self.length-32} mm",
            "width": f"{self.width} mm",
            "groove": True,
            "qty": 1,
        }

    def side_panel(self):
        # length is how tall the cabinet is and width is how deep the cabinet is
        return {
            "name": "side_panel",
            "Edge": "front",
            "length": f"{self.height} mm",
            "width": f"{self.width} mm",
            "groove": True,
            "qty": 2,
        }

    def cleat(self):
        # length is how wide the cabinet is and width is tall the cleat is
        return {
            "name": "cleat",
            "Edge": "front",
            "length": f"{self.length-32} mm",
            "width": f"80 mm",
            "groove": False,
            "qty": 2,
        }

    def backstrip(self):
        # length is how wide the cabinet is and width is tall the backstrip is
        return {
            "name": "backstrip",
            "length": f"{self.length-32} mm",
            "width": f"80 mm",
            "groove": False,
            "qty": 2,
        }

    # ask about when should the cabinet be double doors
    def doors(self):
        # length is how tall the cabinet is and width is how wide it is
        if self.length <= 550:
            door_size = self.length
        else:
            door_size = (self.length-3)/2
        
        return {
            "name": "door",
            "Edge": "all",
            "length": f"{self.height} mm",
            "width": f"{door_size} mm",
            "groove": False,
            "qty": 1,
            "port": True,
        }

    # def base(self, size):
    #     self.size = size
    #     return {"name":"base", "width":f'{self.size-50} mm', "height":f"100 mm", 'groove': False, 'qty': 2},
    #     {"name":"base", "width":f'{self.size-50} mm', "height":f"100 mm", 'groove': False, 'qty': 2}

    def masonite(self):
        # length is how tall the cabinet is and width is how wide the cabinet is
        return {
            "name": "masonite",
            "length": f"{self.length-10} mm",
            "width": f"{self.height-10} mm",
            "groove": False,
            "qty": 1,
        }

    def shelf(self, qty=1):
        # length is how wide the cabinet is and width is deep the cabinet is
        return {
            "name": "shelf",
            "Edge": "front",
            "length": f"{self.length-32} mm",
            "width": f"{self.width-10} mm",
            "groove": False,
            "qty": qty,
        }

    def parts(self):
        return [
            self.bottom(),
            self.side_panel(),
            self.cleat(),
            self.backstrip(),
            self.doors(),
            self.masonite(),
            self.shelf(),
        ]


class Wall(Cabinet):
    def __init__(self, length, width=300, height=760):
        super().__init__(length, width, height)

    def top(self):
        # length is how wide the cabinet is and width is how tall the cabinet is
        return {
            "name": "top_panel",
            "Edge": "front",
            "length": f"{self.length-32} mm",
            "width": f"{self.height} mm",
            "groove": True,
            "qty": 1,
        }

    def parts(self):
        return [
            self.bottom(),
            self.top(),
            self.side_panel(),
            self.backstrip(),
            self.doors(),
            self.masonite(),
            self.shelf(),
        ]

    def shelf(self):
        if self.height <= 300:
            return super().shelf(0)
        else:
            qty = int((self.height) / 300)
            return super().shelf(qty)

    def backstrip(self):
        # length is how wide the cabinet is and width is tall the backstrip is
        return {
            "name": "backstrip",
            "length": f"{self.length-32} mm",
            "width": f"80 mm",
            "groove": False,
            "qty": 3,
        }


def main():
    # project is a list of dicts. Each dict is a summary of parts for each type
    project = []

    order(project)
    output(project)


def order(project):
    while True:
        try:
            no_of_cabinet = int(input(f"Number of total cabinets: "))
            break
        except ValueError:
            print("ERROR! Please enter a number")


    for _ in range(no_of_cabinet):
        while True:
            type=input("Enter type of cabinets (C or W): ").lower()
            if type in ["c","w"]:
                break

        while True:
            try:
                length = int(input("length(mm): "))
                break
            except ValueError:
                print("ERROR! Please enter a number")
        
        if type == "c":
            project.append(Cabinet(length))
        else:
            project.append(Wall(length))

def gui_order(project, type, length):
    if type == "Bottom":
        project.append(Cabinet(length))
    elif type == "Wall":
        project.append(Wall(length))

def summaries(project):
    summary = dict()

    # total length of the project, will be used to calculate the kickplace size
    total_lenght = 0

    # cab is short for cabinet
    for cab in project:
        total_lenght += cab.length
        for part in cab.parts():
            key = (
                part["name"],
                part.get("Edge"),
                part["length"],
                part["width"],
                part["groove"],
                part.get("port"),
            )
            if key not in summary:
                summary[key] = 0
            summary[key] += part["qty"]

    return summary


def output(project):
    wb = Workbook()
    ws = wb.active

    summary = summaries(project)

    # title
    ws.append(["Name", "Edge", "Length", "Width", "Groove", "Port", "Qty"])

    for keys, qty in summary.items():
        name, edge, length, width, groove, port = keys
        if not groove:
            groove = None
        ws.append([name, edge, length, width, groove, port, qty])

    while True:
        try:
            wb.save("test.xlsx")
            break
        except:
            print("Please close file ")
            for i in range(10,0,-1):
                print(f"Retrying in {i}")
                time.sleep(1)

def gui_output(project, project_name):
    wb = Workbook()
    ws = wb.active

    summary = summaries(project)

    # title
    ws.append(["Name", "Edge", "Length", "Width", "Groove", "Port", "Qty"])

    for keys, qty in summary.items():
        name, edge, length, width, groove, port = keys
        if not groove:
            groove = None
        ws.append([name, edge, length, width, groove, port, qty])

    try:
        wb.save(f"{project_name}.xlsx")
        return True
    except:
        return False

if __name__ == "__main__":
    main()


# Future addtions:
# conner unit
# beauty panel
# have one varrible to save all parts then create a function to summaries at the end befor output
# use project name as sheet name
