#!/usr/bin/env python3

# Created by: Crestel Ong
# Created on: October 2021
# The RGB program in python
# This program uses nested loops


def main():
    # this function prints out all the RGB possible combinations
    # declaring
    counter1 = 0
    counter2 = 0
    counter3 = 0

    for counter1 in range(256):  # red
        for counter2 in range(256):  # green
            for counter3 in range(256):  # blue
                print("RGB ({0},{1},{2})".format(counter1, counter2, counter3))


print("\nDone.")


if __name__ == "__main__":
    main()
