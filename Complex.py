class complex:
    def __init__ (self,real,imag):
        self.real=real
        self.imag=imag
    def shownnumber(self):
        print(f"{self.real}i+{self.imag}j")
    def add(self,num2):
        newreal=self.real+num2.real
        newimag=self.real+num2.imag
        return complex(newreal,newimag)
num1=complex(1,6)
num1.shownnumber()
num3=complex(2,5)
num3.shownnumber()
num4=num1.add(num3)
num4.shownnumber

            