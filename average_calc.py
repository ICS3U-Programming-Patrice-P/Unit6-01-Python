#!/usr/bin/env python3

# Created by: Patrice Pat-Odita
# Created on: NOV 22, 2022
# this program generates 10 random numbers using  a for loop and
# print random numbers in a list and calculate the average.
import random


def main():

    # declaring variable
    list_num = []
    # initializing sum and counter
    sum = 0
    counter = 0

    # display opening message to console
    print(
        "This program generates a list of random "
        "numbers between 0 and 100, then calculates the average."
    )
    print("")

    # displays random numbers and calculates average
    for counter in range(10):
        list_num.append(random.randint(0, 100))
        sum = sum + list_num[counter]
        print(
            "{} added to the list at " "position {}".format(list_num[counter], counter)
        )

    # determine if array is full
    # calculate and display average
    for counter in range(10):
        average = sum / 10
    print("")
    print(f"The average is {average}")


if __name__ == "__main__":
    main()
