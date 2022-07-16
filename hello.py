#input name and strip white spaces and capitalize 
#name = input("what's your name? ").strip().title()
#print(f"Hello, {name}" )

def hello(to="World!"):
    print("Hello,", to)
name = input("what's your name? ")
hello(name)