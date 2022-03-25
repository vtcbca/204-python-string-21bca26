#Create two list student and address which contain the name of student and there respected address  print student name with its address

stud=[]
add=[]
count=0
def createList():
    for i in range(5):
        l=input('Enter Student Name : ')
        s=input('Enter Students Address : ')
        stud.append(l)
        add.append(s)
    for i in range(5):
        print(' {} --> {} '.format(stud[i],add[i]))    
createList()
