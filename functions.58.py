def greet(name):
    print("welcome",name)

greet("hafsa")
name=input("enter your name")
greet(name)

def multiplication(n):
    for i in range(1,11):
        print(f"{n}*{i}={n*i}")
multiplication(4)

def even_odd(num):
    if (num%2)==0:
         print(f"{num} is even")
    else:
        print(f"{num} is odd")
even_odd(17)
def dispnum(num,start=1):
    for i in range(start,num+1):
        print(i,end=" ")
dispnum(4)
dispnum(6,3)
def student(*data):
    for i in data:
        print("details are:",i)
student("adiba")
student("adiba",58,"aidsb")
def details(**data):
    print("details are:")
    print("name is:",data["name"])
    print("age is:",data["age"])
    print("occupation is:",data["post"])
details(name="hafsa",age=19,post="student")
def cr(cr1,cr2):
        print(f"girls cr is {cr1}")
        print(f"boys cr is {cr2}")
cr(cr1="hafsa",cr2="abhinav")
def student(firstname,lastname):
 print(firstname,lastname)

student(firstname='adiba',lastname='khushboo')
student(lastname='fatima',firstname='hafsa')
def cr(cr1,cr2):
    print(f"cr1 is {cr1}")
    print(f"cr2 is {cr2}")
cr("abhinav","hafsa")
cr("hafsa","abhinav")
import string
def shift(word,value):
    letters=string.ascii_lowercase
    new=' '
    for i in range(len(word)):
        if word[i] in letters:
            index=letters.index(word[i])
            new=new+letters[(index+word)%26]
        else:
            new=new+word[i]
    return new
word=input("enter ur name")
print(shift(word,1))


    
