# -*- coding: utf-8 -*-

import sys

money_types = [5000, 1000, 500, 100, 50, 10, 5, 1]


def main():
    total = int(sys.argv[1])
    for money_type in money_types:
        if not total:
            print("終了")
            break
        number = total / money_type
        total = total - money_type * number
        print("{0}円は{1}枚".format(money_type, number))


if __name__ == '__main__':
    main()
