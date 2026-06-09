class car:
    def __init__(self):
        self.__fuelling() 
     
    def drive(self):
        print("Driving..!!")
		
    def __fuelling(self): #private method 
        print("Refilling Gas")
	
volvo=car()
volvo.drive()
volvo._car__fuelling() 
volvo.__fuelling() #error because it is private method and cannot be accessed outside the class 