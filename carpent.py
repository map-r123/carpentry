# The cabinet class is an object that returns all the componets that make a cabinet excluding the top
# each function returns a dict with information about that particular panal
class cabinet:
    def __init__(self,length,width=600):
        self.length = length
        

    def bottom(self):
        return {"name":"bottom", "Edge":"front", "length":f'{self.length-32} mm', "heigth":f"600 mm", 'groove': True, 'qty': 1}

    def side_panel(self):
        return {"name":"side_panel", "Edge":"front", "length":'780 mm', "heigth":f"{self.width} mm", 'groove': True, 'qty': 2}
    
    def clit(self):
        return {"name":"clit", "Edge":"front", "length":f'{self.length-32} mm', "heigth":f"80 mm", 'groove': False, 'qty': 2}

    def backstrip(self):
        return {"name":"backstrip", "length":f'{self.length-32} mm', "heigth":f"80 mm", 'groove': False, 'qty': 2}

    # ask about when should there be double doors
    def doors(self):
        if self.length>=600:
            return {"name":"door", "Edge":"all", "length":f'780 mm', "heigth":f"{self.length/2} mm", 'groove': True, 'qty': 2, "port": True}
        else:
            return {"name":"door", "Edge":"all", "length":f'780 mm', "heigth":f"{self.length} mm", 'groove': True, 'qty': 1, 'port': True}

    # def base(self, size):
    #     self.size = size
    #     return {"name":"base", "width":f'{self.size-50} mm', "heigth":f"100 mm", 'groove': False, 'qty': 2},
    #     {"name":"base", "width":f'{self.size-50} mm', "heigth":f"100 mm", 'groove': False, 'qty': 2}

    def masonite(self):
        return {"name":"masonite", "length":f'{self.length-10} mm', "heigth":f"770 mm", 'groove': False, 'qty': 2}

    def shelf(self):
        return {"name":"shelf", "length":f'{self.length-32} mm', "heigth":f"568 mm", 'groove': False, 'qty': 1}
 
    def parts(self):
        return [self.bottom(),
                self.side_panel(),
                self.clit(),
                self.backstrip(),
                self.doors(),
                self.masonite(),
                self.shelf()]

class wall(cabinet):
    def __init__(self, length, width=300):
        super().__init__(length, width)

    def top(self):
        return {'name':"top", 'Edge': "front", 'length':'f"{self.length-32} mm"', 'heigth': f"780 mm", 'groove':True, 'qty':1 }
def main():
    while True:
        try: 
            no_of_cabinet=int(input("Number of cabinets: "))
            break
        except ValueError:
            print("ERROR! Please enter a number")

    project = []

    for _ in range(no_of_cabinet):
        while True:
            try: 
                length=int(input("length(mm): "))
                break
            except ValueError:
                print("ERROR! Please enter a number")
        project.append(cabinet(length))

    summary = dict()
    # total length of the project, will be used to calculate the kickplace size
    total_lenght =0

    for cab in project:
        total_lenght+=cab.length
        for part in cab.parts():
            key = (
            part["name"],
            part.get("Edge"),
            part["length"],
            part["heigth"],
            part["groove"],
            part.get("port")
            )
            if key not in summary:
                summary[key]=0
            summary[key] += part['qty']

    for keys, qty in summary.items():
        name, edge, length, height, groove, port = key
        #currenty to show output
        print(f'keys: {keys} qty: {qty}')

if __name__=="__main__":
    main()
