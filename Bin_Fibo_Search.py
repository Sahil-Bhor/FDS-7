arr1 = []
def lolo():
    no_of_stud = int(input("Enter the number of students: "))
    for _ in range(no_of_stud):
        roll_no = int(input("Enter the student roll no: "))
        arr1.append(roll_no)
    arr1.sort()

    global key
    key = int(input("Enter a key: "))
    choice = int(input("1. Binary Search\n2. Fibonacci Search\n"))
    if choice==1:
        print(Bin_Search())
    elif choice==2:
        print(Fibo())

def Bin_Search():
    first = 0
    last = len(arr1)-1
    mid = 0

    while(first<=last):
        mid = (first+last)//2

        if arr1[mid] < key:
            first = mid + 1  
        elif arr1[mid] > key:
            last = mid - 1  
        else:
            return "Roll no is Present...!"
    return "Roll no is not Present :("


def Fibo():
    size = len(arr1)
    offset = -1
    f0 = 0
    f1 = 1
    f2 = 1
    while (f2<size):
        f0=f1
        f1=f2
        f2=f1+f0
    while f2 > 1:
        index = min(offset+f0, size-1)
        if arr1[index] < key:
            f2 = f1
            f1 = f0
            f0 = f2 - f1
            offset = index
        elif arr1[index] > key:
            f2 = f0
            f1 = f1 - f0
            f0 = f2 - f1
        else:
            return "Roll no is Present"

    if (f2 and index < (size-1) and arr1[size-1]==key):
        return "Roll no is Present"
    return "Roll no not present"

if __name__ == '__main__':
    lolo()
    choose = input("Y to continue and n to exit: ")
    while True:
        if (choose == 'Y'):
            lolo()
        else:
            break        