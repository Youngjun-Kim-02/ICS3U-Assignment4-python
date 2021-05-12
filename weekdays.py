#!/usr/bin/env python3

# created by: Youngjun Kim
# created on: May 2021
# This program checks the number's weekday


def main():
    # this function checks the number's weekday

    # input
    integer_as_string = input("Enter the number of a weekday: ")
    print("")

    # process & output
    try:
        integer_as_number = int(integer_as_string)
        if integer_as_number == 1:
            print("Sunday")
        elif integer_as_number == 2:
            print("Monday")
        elif integer_as_number == 3:
            print("Tuesday")
        elif integer_as_number == 4:
            print("Wednesday")
        elif integer_as_number == 5:
            print("Thursday")
        elif integer_as_number == 6:
            print("Friday")
        elif integer_as_number == 7:
            print("Saturday")
        else:
            print("Invalid number")
    except Exception:
        print("That was not valid input.")


if __name__ == "__main__":
    main()
