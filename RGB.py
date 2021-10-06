#!/usr/bin/env python3

# Created by: Crestel Ong
# Created on: October 2021
# The RGB program in python


def main():
    # this function prints out all the RGB possible combinations

    for counter1 in range(256):
        for counter2 in range(256):
            for counter3 in range(256):
                print("{0},{1},{2}".format(counter1, counter2, counter3))


print("\nDone.")


if __name__ == "__main__":
    main()
