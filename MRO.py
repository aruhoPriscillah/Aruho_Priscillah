class A:
    def feature(self):
        print("Feature from A")

class B(A):
    def feature(self):
        print("Feature from B")

class C(A):
    pass

class D(B, C):
    pass

d = D()
d.feature()  # Output: Feature from B
print(D.mro())  # Shows the MRO: [D, B, C, A, object]
