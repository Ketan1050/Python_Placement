class Car(object):
    
    def __init__(self):
        self.__mileage = 20
        
    def getMileage(self):
        print(self.__mileage)
        
    def setMileage(self,mileage):
        self.__mileage = mileage
        
volvo = Car()
volvo.getMileage()
volvo.setMileage(10)  
volvo.getMileage() 