"""1) Create a class called laptop and create a following variables and functions.
 
 Variables =>Price,Processor,Ram

Create Object HP,DELL,LENOVO."""

class laptop:
    def __int__(self):
        self.Price=""
        self.Processor=""
        self.Ram=""
    def refer_object(display):
        print(f"Laptop price: {display.Price} and the processor is: {display.Processor} total Ram of laptop: {display.Ram}")

HP=laptop()
DELL=laptop()


HP.Price="50,000"
HP.Processor="i3"
HP.Ram="8Gb"
HP.refer_object()
