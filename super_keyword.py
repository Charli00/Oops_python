class dad:
    def __init__(self):
        print("MOney")
    def dad_display(self):
        print("Dad pay fees for me")
class mom(dad):
    def __init__(self):
        super().__init__()
        print("LOVE")
    def mom_display(self):
        print("MOM protect and gives love: ")

class son(mom,dad):
    def __init__(self):
        super().__init__()
        print("Son recived mother and father's love")
    def son_display(self):
        print("son happy")
    


john=son()
john.dad_display()

