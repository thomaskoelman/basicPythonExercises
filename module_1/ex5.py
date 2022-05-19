while True:
    name = input("input your name: ")
    name = name.split(" ")
    if len(name) >= 2:
        break
    print("invalid answer: try again")
print(' '.join(name[1:]) + " " + name[0])