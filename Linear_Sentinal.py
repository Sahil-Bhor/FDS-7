
no_of_stud = int(input("Enter the number of students: "))
arr1 = []
for i in range(no_of_stud):
    roll_no = int(input("Enter the student roll no: "))
    arr1.append(roll_no)
    
key = int(input("Enter a key: "))

def linear_search(arr2):
    for i in range(len(arr2)):
        if arr2[i]==key:
            print(f"\nThe key is present at index no {i}")
        elif key not in arr2:
            print("\nThe key is not present")
            break

n = len(arr1)
def sentinel(arr3):
    for i in range(n):
        last = arr3[n-1]
        if key==(last):
            print(f"\nThe Sentinel key is found at index no {n-1}")  
        elif (last!=key):
            last=key
            if last==arr3[i]:
                print(f"\nSentinel Key is found at index no {i}")
            elif last not in arr3:
                print("\nSentinel key is not present")
                break


if __name__ == '__main__':
    # takin()
    linear_search(arr1)
    sentinel(arr1)