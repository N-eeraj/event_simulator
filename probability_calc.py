def padded(string, num):
    if len(string) < num:
        return "0" * (num - len(string)) + string
    return string

event = int(input("Welcome\n1. Coin Toss\n2. Die Roll\n3. Card Draw\nSelect Option: "))

if event == 1:
    possibility = ("Head", "Tail")
    coins = int(input("Enter number of coins: "))
    print("\nPossible Outcomes: ")
    for chances in range(2 ** coins):
        for outcome in list(padded(str(bin(chances))[2:], coins)):
            print(possibility[int(outcome)], end = " ")
        print()
    print(f"Probability for any outcome: {1 / 2 ** coins * 100}%")
elif event == 2:
    dice = int("Enter number of dice thrown: ")
elif event == 3:
    cards = int("Enter number of cards picked: ")
else:
    print("Invalid Option")