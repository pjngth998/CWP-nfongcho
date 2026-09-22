import sys

def shrink(txt):
    return txt[:8]

def enlarge(text):
    add = 8 - len(text)
    for i in range(add):
        text = text + "Z"
    return text

if len(sys.argv) == 1:
    print("none")
else:
    for i in sys.argv[1:]:
        if len(i) >= 8:
            print(shrink(i))    
        else:
            print(enlarge(i))