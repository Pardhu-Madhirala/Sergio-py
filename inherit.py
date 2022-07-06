class king:
    def mava(self):
        print("mava method:")
    def mava(self):
        print("mava bro")
    def mava(self):
        print("mava bros")
class queen(king):
    def mava(self,a):
        print("inherited")


a1=queen()
a1.mava(1)