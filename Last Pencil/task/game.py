import random

n_pencils = 0
index = 0


def print_message():
    print("|" * n_pencils)
    print(f"{players[index]}'s turn:")


def bot_play():
    global n_pencils
    global index

    losing_positions = range(1, (n_pencils + 1), 4)
    if n_pencils not in losing_positions:
        for position in losing_positions:
            if position + 1 == n_pencils:
                bot_value = 1
                break
            elif position + 2 == n_pencils:
                bot_value = 2
                break
            elif position + 3 == n_pencils:
                bot_value = 3
                break
    else:
        if n_pencils == 1:
            bot_value = 1
        else:
            bot_value = random.randint(1, 3)

    if index == 1:
        index = 0
    elif index == 0:
        index = 1
    n_pencils -= bot_value

    print(bot_value)


print("How many pencils would you like to use:")
running = True
while running:
    try:
        n_pencils = int(input())
    except ValueError:
        print("The number of pencils should be numeric")
    else:
        if n_pencils == 0:
            print("The number of pencils should be positive")
        elif n_pencils < 0:
            print("The number of pencils should be numeric")
        else:
            who_first = True
            while who_first:
                print("Who will be the first (John, Jack):")
                first = input()

                players = ["Jack", "John"]
                index = 0

                if first not in (players[0], players[1]):
                    print(f"Choose between {players[0]} and {players[1]}")
                    continue
                else:
                    who_first = False
                    if first == "Jack":
                        index = 0
                    elif first == "John":
                        index = 1

                    while n_pencils > 0:
                        if first == "John":
                            print_message()

                            try:
                                value = int(input())
                            except ValueError:
                                print("Possible values: '1', '2', '3'")
                            else:
                                if value not in (1, 2, 3):
                                    print("Possible values: '1', '2', '3'")
                                elif value > n_pencils:
                                    print("Too many pencils were taken")
                                else:
                                    if index == 1:
                                        index = 0
                                    elif index == 0:
                                        index = 1
                                    n_pencils -= value

                                    if n_pencils > 0:
                                        print_message()
                                        bot_play()
                        elif first == "Jack":
                            print_message()

                            if players[index] == "Jack":
                                bot_play()

                            if n_pencils > 0:
                                print_message()
                                try:
                                    value = int(input())
                                except ValueError:
                                    print("Possible values: '1', '2', '3'")
                                else:
                                    if value not in (1, 2, 3):
                                        print("Possible values: '1', '2', '3'")
                                    elif value > n_pencils:
                                        print("Too many pencils were taken")
                                    else:
                                        if index == 1:
                                            index = 0
                                        elif index == 0:
                                            index = 1
                                        n_pencils -= value

                    print(f"{players[index]} won!")
                    running = False
                    break
