!/usr/bin/env python3

# Created by: Jack D'Angelo
# Created on: October 2019
# This program says if a number is + or - or ==


def main():
    # input
    number = int(input("Enter a posistve or negative number: "))

    # process
    if number < 0:
        # output
        print()
        print("-")

    # process
    elif number == 0:
        # output
        print()
        print("0")

    # process
    else:
        # output
        print()
        print("+")


if __name__ == "__main__":
    main()
