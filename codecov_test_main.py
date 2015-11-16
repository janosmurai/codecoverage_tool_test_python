__author__ = 'murai'

def test_function(a, b):
    if a > b:
        while a > b:
            b += 1
        print("a is greater then b")
    elif a == b:
        print("a and b are equal")
    else:
        print("b is greater then a")

    for i in range(a):
        if b and (a < 200):
            print(i * b)

test_function(10,20)