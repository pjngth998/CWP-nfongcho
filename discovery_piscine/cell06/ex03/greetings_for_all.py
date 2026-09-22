def greetings(name=None):
    if name is None:
        print("Hello, noble stranger.")
    elif not str(name).isalpha():
        print("Error! It was not a name.")
    else:
        print(f"Hello, {name}")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
