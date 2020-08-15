
def strings(x, y):
    if type(x) != str and type(y) != str:
        print ("0")
    elif x == y:
        print("1")
    elif x != y and len(x) > len(y):
        print ("2")
    elif x != y and y == "learn":
        print ("3")
    else:
        print ("4")
    

strings("ghbdtn", "learn")
