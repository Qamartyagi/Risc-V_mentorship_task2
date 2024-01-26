list = []

def inp1():
    while True:
        val=int(input("Enter the no of element multiple of 10 : "))

        if(val%10==0):
            for i in range(val):
                list.append(int(input("Enter the element : ")))
            break
        else:
            print("Invalid input size. ")
            print("Enter the no of element in multiple of 10")

inp1()


print("The list with the lement removed which are  multiple of 2 or 3 is : ",list)
for j in list:
    if(j%2==0 or j%3==0):
        continue
    else:
        print(j)