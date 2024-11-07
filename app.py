print("Type 'listapps' to list the apps")
cont = True
while cont:
    x = input("WalterOS/miniapps::>")
    if x == "listapps":
        import listapps
    elif x == "clock":
        import clock
    elif x == "quit":
        cont = False
        print("Bye")
        print("")
        break
