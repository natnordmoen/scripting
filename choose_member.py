#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def choose_groups(teammembers):
    random.shuffle(teammembers)

    while len(teammembers) > 3:
        print(teammembers.pop() + " og " + teammembers.pop(1))
    else:
        print(' og '.join(map(str,teammembers)))
        teammembers.clear()


def main():
    choose_groups(input("Hvem er her?").split(", "))


if __name__ == "__main__":
    main()