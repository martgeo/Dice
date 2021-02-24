#  Dice Simulator
#  Option for number of eyes on dice through 'size'
#  press enter to keep rolling
#  type 'END' to stop

import random


def choosesize():
    while True:
        try:
            size = int(input("Please enter the size of your dice: "))
        except ValueError:
            size = None

        if size is None:
            print("Please enter number only!")
        elif size <= 0:
            print("Please enter number above 0!")
        else:
            break
    return size


def rolldice(size):
    dice = [num for num in range(1, size + 1)]
    return print(random.choice(dice))


def main():
    size = choosesize()
    play = input("Press ENTER to roll or type 'END' to end!")
    while str(play) != "END":
        rolldice(size)
        play = input()
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
