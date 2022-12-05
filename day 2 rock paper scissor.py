# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 13:36:01 2022

Day 2 advent of code 2022

Rock Paper Scissor Tournament Score

@author: adho3
"""
import os
import pandas as pd
import numpy as np
print(os.getcwd())

letter_map = {'A' : 'rock',
              'B' : 'pap',
              'C' : 'sci',
              'X' : 'rock',
              'Y' : 'pap',
              'Z' : 'sci',
              }

outcome_dict = {'rockpap': 6, 
                'papsci' : 6, 
                'scirock' : 6,
                'rockrock' : 3,
                'pappap' : 3,
                'scisci' : 3,
                'paprock' : 0,
                'rocksci' : 0,
                'scipap' : 0,
                'rock' : 1, 
                'pap' : 2, 
                'sci' : 3
                }


strategy_data = open("day_2_input.txt", "r")

split_by_blank_row = strategy_data.read().split('\n')

#now split within the lists as well
parsed_data = [elf.split(" ") for elf in split_by_blank_row]

parsed_data_pdf = pd.DataFrame(parsed_data, columns=["Opponent", "You"])

parsed_data_clear_pdf = parsed_data_pdf.replace(letter_map)

parsed_data_clear_pdf['Concat'] = parsed_data_clear_pdf['Opponent'] + parsed_data_clear_pdf['You']

final_scores = parsed_data_clear_pdf[['You', 'Concat']].replace(outcome_dict)

final_scores['Total_Score'] = final_scores['You'] + final_scores['Concat']

print(final_scores['Total_Score'].sum())