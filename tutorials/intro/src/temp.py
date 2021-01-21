class Temp:
    """ Klass för att hantera temperaturer i Kelvin, Fahrenheit och Celsius """

    nollC = 273.15                        
    nollF = 255.3722                   #F-nollan i Kelvin

    def __init__(self):
        self.K = 0                     #Temperatur i Kelvin

    def setK(self,K): 
        self.K = K

    def setC(self,C):
        self.K = Temp.nollC+C

    def setF(self,F): 
        self.K = Temp.nollF+5*F/9

    def getK(self):   
        return self.K

    def getC(self):   
        return self.K-Temp.nollC

    def getF(self):   
        return (self.K-Temp.nollF)*9/5

def main():
    t = Temp()
    t.setC(20)
    print(f"{round(t.getF())} är temperaturen i Fahrenheit")

main()
