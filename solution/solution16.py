#WAS to enter any string and check it is palindrom or not
s=input("Enter any string:")
c=s
c=s[::-1]
if(c==s):
    print("{} is a palindrom string".format(s))
else:
    print("{} is not a palindrom string".format(s))
