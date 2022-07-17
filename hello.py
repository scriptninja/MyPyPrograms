#input name and strip white spaces and capitalize 

def hello(to="World!"):
    print("Hello,", to)
name = input("what's your name? ").strip().title()
hello(name)