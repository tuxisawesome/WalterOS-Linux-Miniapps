import clock, listapps
print("Type 'listapps' to list the apps")
cont = True
while cont:
    x = input("WalterOS/miniapps::>")
    if x == "listapps":
        listapps.run()
    elif x == "date":
        clock.run()
    elif x == "quit":
        cont = False
        print("Bye")
        print("")
        break
