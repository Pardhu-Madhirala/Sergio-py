class python:
    def __init__(self):
        self.ch="telusko"
        self.IN =self.legend()
    def telusko(self):
        print("loyal legend:",self.ch)
        #self.IN.show()
    class legend:
        def __init__(self):
            self.age=23
        def show(self):
            print("hello inner class")
obj=python()
obj.telusko()
lap2=python.legend()
lap2.show()