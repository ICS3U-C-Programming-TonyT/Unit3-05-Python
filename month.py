#!/usr/bin/env python3
# Created By: Tony Tran
# Date: Oct. 20, 2023
# This is program will tell you what month it is using the number from 1,12.


def main():
    month_num = int(input("Give me the month number from 1,12:\n"))
    months = {
        1: f"{month_num} is January",
        2: f"{month_num} is February",
        3: f"{month_num} is March",
        4: f"{month_num} is April",
        5: f"{month_num} is May",
        6: f"{month_num} is June",
        7: f"{month_num} is July",
        8: f"{month_num} is August",
        9: f"{month_num} is September",
        10: f"{month_num} is October",
        11: f"{month_num} is November",
        12: f"{month_num} is December",
    }
    print(months.get(month_num, "Month number is not valid"))


if __name__ == "__main__":
    main()
