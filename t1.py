

def nameN(name,age):
    
    print("Hello", name)
    print("your age is ",age)
    



nameN("lamar",19)

def add(a,b):
    
    if a>0 and b>0:
        print (a+b)
    else:
        print("invalid input<<please enter positive numbers only>>")


add(9,3)
add(100,200)


def sayhello(*names):
    
    
    

    for n in names:
        print("hello",n)


sayhello("lamar","lama","dyala","lina","lolo")


def introduce(name, age=0,city="unknown"):
    
    print("Hello, my name is",name)
    print("I am",age,"years old")
    print("I live in",city)
    
    
    

introduce("Lamar")
print("*"*50)
def showskills (**skills):
    
    print("My skills are:")
    for skill, value in skills.items():
        print(skill + ":", value)

showskills(programming="python",math="algebra",science="physics")

print("*"*50)

