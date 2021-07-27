event = int(input("Welcome\n1. Coin Toss\n2. Die Roll\n3. Card Draw\nSelect Option: "))

if event == 1:
    possibility = ("Head", "Tail")
    coins = int(input("Enter number of coins: "))
    print(f"Probability for any outcome: {1 / 2 ** coins * 100}%")
elif event == 2:
    possibility = tuple(range(1, 7))
    dice = int(input("Enter number of dice thrown: "))
    print(f"Probability for any outcome: {1 / 6 ** dice * 100}%")
elif event == 3:
    cards = int(input("Enter number of cards picked: "))
    print(f"Probability for any outcome: {1 / 52 ** cards * 100}%")
else:
    print("Invalid Option")