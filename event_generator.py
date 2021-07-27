from random import randint, choice

while True:
    event = int(input("\nMain Menu\n1. Coin Toss\n2. Die Roll\n3. Spin a Bottle\n4. Exit\nSelect event you want to simulate: "))
    if event == 1:
        print("Coin Toss")
        print(choice(["Head", "Tail"]))
    elif event == 2:
        print("Die Roll")
        for i in range(int(input("Enter Number of Dice: "))):
            print(randint(1, 6), end = ", ")
        print()
    elif event == 3:
        print("Bottle Spin")
        players = list()
        for i in range(int(input("Enter Number of Players: "))):
            players.append(input("Enter Name: "))
        while True:
            print(choice(players))
            if input("Enter Y to spin again: ").lower() != "y":
                break
        del players
    elif event == 4:
        print("Exiting...")
        break
    else:
        print("Invalid Option\nTry again")