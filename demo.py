#!/usr/bin/env python

import sys

vowels=['a', 'i', 'e', 'o', 'u', 'y', 'æ', 'ø', 'å']

def make_rover_without_comprehension(word):
    rover_word = ""
    for letter in word.lower():
        if letter not in vowels:
            rover_word += (letter + 'o' + letter)
        else:
            rover_word += letter
    return rover_word

def make_rover(word):
    return "".join([(letter + 'o' + letter) if letter not in vowels else letter for letter in word.lower()])


def demo_user_input():
    name = input("Hei! Hva heter du?")
    print(make_rover(name))


#demo_user_input()

def demo_file_input():
    file_name = input("Har du en fil?")
    f = open(file_name, "r")
    print(f.read())

#demo_file_input()

def demo_write_to_file():
    name = input("Hei! Hva heter du? ")
    f = open("demo2.txt", "a")
    f.write(make_rover(name))
    f.close()

demo_write_to_file()
