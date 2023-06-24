import os
import json
from prettytable import PrettyTable
mytable = PrettyTable()
def cls():
    os.system('cls' if os.name=="nt" else "clear")
f = open("sathvikdata.txt","r")
alphabet = "abcdefghijklmnopqrstuvwxyz"
preorderalpha = "phtdlrxbfjnqsvyacegikmouwz"
preordernum = "421365879"
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.contactlist = dict()
class Node1:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.contactlist = dict()
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root
def inorder(root):
    if root:
        print(root.val,root.contactlist,end=' ')
        inorder(root.left)
        inorder(root.right)
r = Node('p')
inorderaplha = "htdlrxbfjnqsvyacegikmouwz"
for i in inorderaplha:
    r = insert(r,i)
r1 = Node('4')
inordernum = "26135879"
for i in inordernum:
    r1 = insert(r1,i)
def search(root,ch):
    if root.val == ch:
        return root
    elif root.val < ch:
        return search(root.right, ch)
    else:
        return search(root.left, ch)
    return root
def addcontact(root,name,phonenum):
    root = search(root,name[0])
    if name in root.contactlist.keys():
        print("Contact already exists!")
    else:
        root.contactlist.update({name:phonenum})
        addcontactnum(r1,name,phonenum)
def addcontactnum(root,name,phonenum):
    root = search(root,phonenum[0])
    if phonenum in root.contactlist.keys():
        print("Contact already exists!")
    else:
        root.contactlist.update({phonenum:name})
        print("Successfully added!")
    #print(root.contactlist)
def searchmycontact(r,ch,name):
    flag = 0
    temp = search(r,ch)
    if(name in temp.contactlist.keys()):
        cls()
        print("Name :",name+"\n"+"Contact no. :",temp.contactlist.get(name))
    else:
        cls()
        print("Results for",name,":")
        for i in temp.contactlist:
            if name in i:
                flag = 1
                print(i,temp.contactlist[i])
        if(flag==0):
            print("No contacts found :(")
def displayphonbook(root):
    mytable.clear_rows()
    mytable.field_names = ["Alphabet","Name","Contact Nunber"]
    for i in alphabet:
        temp = search(r,i)
        if(temp.contactlist == {}):
            continue
        for j in temp.contactlist:
            mytable.add_row([i,j,temp.contactlist[j]])
    print(mytable)
def deletecontact(root,root1):
    while(True):
        name = str(input("Enter name or phonenumber ")).lower()
        temp = name
        if name.isnumeric():
            root = search(root1,name[0])
        else:
            root = search(root,name[0])
        if(root==None):
            print("Error input!")
        else:
            ans = list(filter(lambda x:(name in x),root.contactlist.keys()))
            ans2 = list(filter(lambda x:(name == x),root.contactlist.keys()))
            if len(ans)==0:
                print("No search results found!. Try some other filter :)")
            elif(len(ans)==1):
                temp = ans[0]
                print("Are you sure to delete the contact",temp,'-->',root.contactlist[temp],"?")
                option = str(input()).lower()
                if option=="yes":
                    print("Successfully deleted!")
                    del root.contactlist[temp]
                    break
                else:
                    break
            elif len(ans2)==1:
                temp = ans2[0]
                print("Are you sure to delete the contact",temp,'-->',root.contactlist[temp],"?")
                option = str(input()).lower()
                if option=="yes":
                    print("Successfully deleted!")
                    del root.contactlist[temp]
                    break
                else:
                    break
            else:
                print("Found multiple result matches , try more precision in name")
def editcontact(root):
    while(True):
        name = str(input("Enter name : ")).lower()
        temp = name
        root = search(root,name[0])
        if(root==None):
            print("Error input!")
        else:
            ans = list(filter(lambda x:name in x,root.contactlist.keys()))
            if len(ans)==0:
                print("No search results found! Try some other filter :)")
            elif(len(ans)==1):
                temp = ans[0]
                print("Enter the new name if any for",temp,": ")
                name = str(input()).lower()
                while name[0].isalpha() != True:
                    print("Name shall start with an alphabet!")
                    name = str(input("Enter name : "))
                print("Enter new contact if any for",root.contactlist[temp],": ")
                phno = str(input()).lower()
                while phno.isnumeric() != True or phno[0]=='0':
                    print("Enter only numericals!")
                    phno = str(input("Enter your phonenum : "))
                del root.contactlist[temp]
                addcontact(root,name,phno)
                break
            else:
                print("Found multiple result matches , try more precision in name")
def writedata(root,root1):
    f = open("sathvikdata.txt","a")
    for i in preorderalpha:     #use loading sequence technique
        temp = search(root,i)
        f.write(json.dumps(temp.contactlist))
        f.write('\n')
    for i in preordernum:
        temp = search(root1,i)
        f.write(json.dumps(temp.contactlist))
        f.write('\n')
def loaddata(root,root1):
    for i in preorderalpha:
        temp = search(root,i)
        data = f.readline()
        temp.contactlist = json.loads(data)
        #print(temp.val,temp.contactlist,sep='=====')
    for i in preordernum:
        temp = search(root1,i)
        data = f.readline()
        temp.contactlist = json.loads(data)
def main():
    loaddata(r,r1)
    print("S os Phonebook : ")
    while(True):
        print("1)Add contact\n2)Search contact\n3)Display phonebook\n4)inorder check\n5)Edit\n6)Delete\n7)exit")
        option = input("Enter an operation : ")
        cls()
        if(option=='1'):
            name = str(input("Enter name : ")).lower()
            while name[0].isalpha() != True:
                print("Name shall start with an alphabet!")
                name = str(input("Enter name : "))
            phonenum = str(input("Enter your phonenum : "))
            while phonenum.isnumeric() != True or phonenum[0]=='0':
                print("Enter only numericals!")
                phonenum = str(input("Enter your phonenum : "))
            addcontact(r,name,phonenum)
        elif(option=='2'):
            ch = str(input("Enter the name/phone_number : ")).lower()
            if ch.isnumeric() :
                searchmycontact(r1,ch[0],ch)
            else:
                searchmycontact(r,ch[0],ch)
        elif(option=='3'):
            displayphonbook(r)
        elif(option=='4'):
            inorder(r)
            print()
            inorder(r1)
            print()
        elif(option=='5'):
            editcontact(r)
        elif(option=='6'):
            deletecontact(r,r1)
        else:
            f = open("sathvikdata.txt","w")
            writedata(search(r,'p'),search(r1,'4'))
            f.close()
            return 0
main()