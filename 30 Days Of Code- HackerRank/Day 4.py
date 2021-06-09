class Person:
    def __init__(self,initialAge):
        self.initialAge=0
        if (initialAge<0):
            print("Age is not valid, setting age to 0.")
        else:
            self.initialAge=initialAge
            
    def amIOld(self):
        if (self.initialAge<13):
            print("You are young.")
        elif (self.initialAge<18):
            print("You are a teenager.")
        else:
            print("You are old.")
            
    def yearPasses(self):
        self.initialAge+=1
                
t = int(input())