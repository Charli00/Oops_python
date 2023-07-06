"""1) Create a class called laptop and create a following variables and functions.
 
 Variables =>Price,Processor,Ram

Create Object HP,DELL,LENOVO."""

class laptop:
    Price=""
    Processor=""
    Ram=""
    def buy_Computer_shop_01(self):
        print("Saravana stores ")
        print("color: white")
    def buy_Computer_shop_02(self):
        print("Agni computer:")
        print("colour: black")
        print("model: 2021")

DELL=laptop()
DELL.Price="50,000"

print(DELL.Price)
DELL.buy_Computer_shop_01()



