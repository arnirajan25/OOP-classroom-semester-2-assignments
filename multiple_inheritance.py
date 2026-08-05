#Multiple Inheritance & MRO Create classes A, B, and C. Let C inherit from both A and B.Add methods in each class with the same name. Print the Method Resolution Order (MRO) of C.

class A:   
    def info(self):
        print("Nirajan")

class B():
    def info(self):
        print("studies BCS")

class C(A,B):
    def info(self):
        print("likes programming!")

a = C()
a.info()
print(C.mro())
