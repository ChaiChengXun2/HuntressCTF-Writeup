import base64

def shift17(Beets):
    return chr(int(Beets) - 17)

def getLeft(Grapes):
    return Grapes[:3]

def getRight(Jelly):
    return Jelly[3:]

def Nuts(Milk):
    OatMilk = ""
    while len(Milk) > 0:
        OatMilk += shift17(getLeft(Milk))
        Milk = getRight(Milk)
    return OatMilk

def reverse(Cows):
    return Cows[::-1]

def Tragedy():
    Apples = "129128136118131132121118125125049062118127116049091088107132106104116074090126107132106104117072095123095124106067094069094126094139094085086070095139116067096088106065107085098066096088099121094101091126095123086069106126095074090120078078"
    Water = Nuts(Apples)
    print(base64.b64decode(Water[16:]).decode().split("\"")[1])

Tragedy()
