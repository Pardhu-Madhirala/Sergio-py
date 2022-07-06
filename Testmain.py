'''print("Testmain coming partner:")
if __name__=="__main__":
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
    DK(2,6)


class Student:
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age
s = Student("John", 101, 22)
print(getattr(s, 'name'))
setattr(s, "age", 23)

print(getattr(s, 'age'))

print(hasattr(s, 'id'))
delattr(s, 'age')
delattr(s,'name')
print(s.name)
class Real:
    def __init__(oyo,car,color):
        print("iam legend")
        oyo.car=car
        oyo.color=color
        print("iam legend")
        print(oyo.car, oyo.color)
    def mama(oyo):
        print(oyo.car,oyo.color)
objects=Real("TATA","Legend")
objects.mama()'''
def search(list,m):
    for i in list:
        if i==m:
            print("true")
    else:
        print("king")


list=[1,2,3,4,5,6]
m=5
search(list,m)




