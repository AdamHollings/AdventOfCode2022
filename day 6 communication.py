# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 21:15:53 2022

Day 6 puzzle

@author: adho3
"""

import os

print(os.getcwd())

puzzle_input = open("day_6_input.txt", "r").readlines()

window_list = []
marker = None

for counter, signal in enumerate(puzzle_input[0]):
    window_list.append(signal)
    if len(window_list) > 4:
        window_list = window_list[1:5]
    print(counter+1, " ", window_list)
    if counter > 4 and sorted(window_list) == sorted(list(set(window_list))):
        print(counter+1, " is the signal value. 4 unique character occur before this one")
        marker = counter
        break

if marker != None:
    packet = puzzle_input[0][marker:]
    
    packet_list = []
    for counter_two, piece in enumerate(packet):
        packet_list.append(piece)
        if len(packet_list) > 14:
            packet_list = packet_list[1:15]
        print(marker+counter_two+1, " ", packet_list)
        if counter_two > 14 and sorted(packet_list) == sorted(list(set(packet_list))):
            print(marker+counter_two+1, " is the message value. 14 unique character occur before this one")
            break
