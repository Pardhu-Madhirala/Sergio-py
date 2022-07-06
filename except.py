import module
'''if __name__=="__main__":
    a=10
    b=5
    def DK(a,b):

        print(a/b)

    def Royals(RCB):
        def ABD(a,b):
            print(a,b)
            if a<b:
                a,b=b,a
                print(a,b)
            return RCB(a,b)
        return ABD
    DK=Royals(DK)
    DK(2,6)'''
class z:
    def __init__(self,a):
        self.a=a
    def __add__(self, b):
        return self.a+b.a
c=z(1)
d=z(2)
print(c+d)