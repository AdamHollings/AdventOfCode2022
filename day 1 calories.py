# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 09:42:40 2022

Advent of code day 1

@author: adho3
"""

import os
import pandas as pd

print(os.getcwd())


calories_data = open("day_1_input.txt", "r")

split_by_blank_row = calories_data.read().split('\n\n')

#now split within the lists as well
parsed_data = [list(map(int, elf.split("\n"))) for elf in split_by_blank_row]

total_calories_elf = [sum(elf) for elf in parsed_data]

max_calories_elf = max(total_calories_elf)

total_top_3_elf =  sum(sorted(total_calories_elf, reverse=True)[:3])
