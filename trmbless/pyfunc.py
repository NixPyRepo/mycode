#!/usr/bin/env python3

from blessings import Terminal

t = Terminal()

print(t.clear())

print(t.bold("Hi there!"))

print(t.movedown())

print(t.bold_red_on_bright_green("It hurts my eyes"))

print(t.move_down+t.bold_underline_black_on_yellow('Look! A 1997 web page! No, the font would have to be blinking'))