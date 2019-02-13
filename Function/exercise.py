def first():
    print("This is the first function")

def second(intVal):
        return intVal*2

def third(int1,int2):
    return int1*int2

def fourth(a,b,c):
    print(third(second(a),b)*c)

first()

fourth(4,6,7)
