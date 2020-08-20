#write a program to multiply the two largest numbers in the list
list=[]
n=int(input("enter the elements of the list:\n"))
for i in range(0,n):
    ele=int(input("enter the elements: "))
    list.append(ele)
print(list)
#a=max(list)
#print(a)
list.sort()
a=list[-1]
b=list[-2]
c=a*b
print("the product is:{}" .format(c))
