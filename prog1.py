#string
a=input("enter any string:\n")
n=len(a)
print("length is:{}".format(n))
vowel=0
lower=0
upper=0
count=0
for i in range(0,n):
    if(a[i]!=''):
        if a[i].isalpha():
           if a[i].isupper():
              upper=upper+1
           if a[i].islower():
              lower=lower+1
           if (a[i]=='a' or a[i]=='e' or a[i]=='o' or a[i]=='i' or a[i]=='u' or a[i]=='U' or a[i]=='O' or a[i]=='I' or a[i]=='E' or a[i]=='A'):
               vowel=vowel+1
        elif a[i].isdigit():
            break
        else:
            count=count+1

print("the special upper characters are {}".format(upper))        
print("the special lower characters are {}".format(lower))              
print("the special special characters are {}".format(count))   
print("the special vowels characters are {}".format(vowel))

        
