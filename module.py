'''class legend:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def methods(self):
        print("hello oops",self.a,self.b)
    def lucky(self):
        print("hello champ",self.a,self.b)
com1=legend(1,2)#object creating in python
#legend.methods(com1)
#com1.methods()
com1.lucky()
n=12
m=12
print(id(m))
print(id(n))'''

class Monster:
    def KGF(self):
        print("Monster entered to KGF:")
    def Bombay(self,a,b):
        print("a,b values :",a,b)
Bng=Monster()
Monster.KGF(Bng)
Bng.Bombay(6,5)