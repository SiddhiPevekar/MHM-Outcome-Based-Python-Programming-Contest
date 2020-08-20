#sort numbers and alphabets
s=input("enter any string:\n")
def arrange(s):
     p=''.join(sorted(s)) 
     return p
res=arrange(s)
print(res)
