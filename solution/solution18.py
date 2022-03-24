#WAS to enter five string in a list and print those string whose length has even no of character without using function

def createList():
    l=[]
    for i in range(5):
        s=input("Enter string:")
        l.append(s)
    return(l)
a=createList()
for i in a:
    print(i)


def evenNoString(l):
    for i in l:
        count=0
        for j in i:
            count=count+1
        if(count%2==0):
            pass
    return(i)
c=evenNoString(i)
print(c)
