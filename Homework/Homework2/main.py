from Array import Array

def main():
    a1 = Array(5)

    a1[0] = 1
    a1[1] = 6
    a1[2] = 3

    print("a1: ")
    print(a1)

    a2 = Array(4)

    a2[0] = 2
    a2[1] = 3

    print("a2: ")
    print(a2)

    a3 = Array(5)
    
    a3[0] = 1
    a3[1] = 6
    a3[2] = 3

    print("a3: ")
    print(a3)

    print("Compare a1 and a3: ")
    if a1 == a3:
        print("a1 equal a3")
    else:
        print("a1 not equal a3")
    
    print("Compare a2 and a3: ")

    if a2 == a3:
        print("a2 equal a3")
    else:
        print("a2 not equal a3")

    print("-------------")

    print("set a1[0] = 9")

    try:
        a1[0] = 9
    except IndexError as error:
        print(error)

    print("a1: ")
    print(a1)

    print("Try to set a1[3] = 5 which is beyond logical size")

    try:
        a1[4] = 5
    except IndexError as error:
        print(error)
    
    print("Try to set non-last index = 0")
    try:
        a3[1] = None
    except IndexError as error:
        print(error)

    
    
main()


