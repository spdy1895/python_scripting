globalVar = "This is global"


def myFunction():
    localVar = "This is local"
    globalVar = "This is local"
    print("myFunction - localVar:" + localVar)
    print("myFunction- globalVar:" + globalVar)


print("global- globalVar:" + globalVar)
myFunction()
