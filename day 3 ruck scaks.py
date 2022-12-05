# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 13:36:01 2022

Day 3 advent of code 2022

Ruck Sack Priority

@author: adho3
"""
import os
import pandas as pd
import numpy as np

def split_list(a_list)-> list:
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

print(os.getcwd())

priority_map = {'a':1  ,
'b':2  ,
'c':3  ,
'd':4  ,
'e':5  ,
'f':6  ,
'g':7  ,
'h':8  ,
'i':9  ,
'j':10 ,
'k':11 ,
'l':12 ,
'm':13 ,
'n':14 ,
'o':15 ,
'p':16 ,
'q':17 ,
'r':18 ,
's':19 ,
't':20 ,
'u':21 ,
'v':22 ,
'w':23 ,
'x':24 ,
'y':25 ,
'z':26 ,
'A':27 ,
'B':28 ,
'C':29 ,
'D':30 ,
'E':31 ,
'F':32 ,
'G':33 ,
'H':34 ,
'I':35 ,
'J':36 ,
'K':37 ,
'L':38 ,
'M':39 ,
'N':40 ,
'O':41 ,
'P':42 ,
'Q':43 ,
'R':44 ,
'S':45 ,
'T':46 ,
'U':47 ,
'V':48 ,
'W':49 ,
'X':50 ,
'Y':51 ,
'Z':52 
              }


strategy_data = open("day_3_input.txt", "r")

split_by_blank_row = strategy_data.read().split('\n')

#now split within the lists as well
parsed_data = [list(split_list(backpack)) for backpack in split_by_blank_row]

common_items = [''.join(set(bag[0]).intersection(bag[1])) for bag in parsed_data]

mapped_common_items = pd.DataFrame(common_items, columns=['Priority']).replace(priority_map)

sum_priorities = mapped_common_items['Priority'].sum()

col1, col2         = 'Opponent', 'You'
conditions  = [ (parsed_data_clear_pdf[col1] == 'rock') & (parsed_data_clear_pdf[col2] == 'lose'), 
                (parsed_data_clear_pdf[col1] == 'pap') & (parsed_data_clear_pdf[col2] == 'lose'),
                (parsed_data_clear_pdf[col1] == 'sci') & (parsed_data_clear_pdf[col2] == 'lose'),
                (parsed_data_clear_pdf[col1] == 'rock') & (parsed_data_clear_pdf[col2] == 'draw'), 
                (parsed_data_clear_pdf[col1] == 'pap') & (parsed_data_clear_pdf[col2] == 'draw'),
                (parsed_data_clear_pdf[col1] == 'sci') & (parsed_data_clear_pdf[col2] == 'draw'),
                (parsed_data_clear_pdf[col1] == 'rock') & (parsed_data_clear_pdf[col2] == 'win'), 
                (parsed_data_clear_pdf[col1] == 'pap') & (parsed_data_clear_pdf[col2] == 'win'),
                (parsed_data_clear_pdf[col1] == 'sci') & (parsed_data_clear_pdf[col2] == 'win')
                ]
choices     = [ "sci", 'rock','pap',"rock", "pap", "sci", "pap", "sci", "rock" ]
    
parsed_data_clear_pdf["Win_Play"] = np.select(conditions, choices, default=np.nan)

parsed_data_clear_pdf['Concat'] = parsed_data_clear_pdf['Opponent'] + parsed_data_clear_pdf['Win_Play']

final_scores = parsed_data_clear_pdf[['Win_Play', 'Concat']].replace(outcome_dict)

final_scores['Total_Score'] = final_scores['Win_Play'] + final_scores['Concat']

print(final_scores['Total_Score'].sum())