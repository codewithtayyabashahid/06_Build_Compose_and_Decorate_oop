class A:
    def show(self):
        print("Show from Class A")

class B(A):
    def show(self):
        print("Show from Class B")

class C(A):
    def show(self):
        print("Show from Class C")

class D(B, C): 
    pass

d = D()
d.show()  

print(D.__mro__) 
