# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 13:36:01 2022

Day 4 advent of code 2022

Ruck Sack Priority

@author: adho3
"""
import os
import pandas as pd
import numpy as np
import re

def expand_ranges(s):
    return re.sub(
        r'(\d+)-(\d+)',
        lambda match: ','.join(
            str(i) for i in range(
                int(match.group(1)),
                int(match.group(2)) + 1
            )   
        ),  
        s
    )

print(os.getcwd())

strategy_data = open("day_4_input.txt", "r")

split_by_blank_row = strategy_data.read().split('\n')
split_by_comma = [rota.split(',') for rota in split_by_blank_row]

overlap_count = 0
partial_overlap_count = 0

for line in split_by_comma:

    elf1 = line[0]
    elf2 = line[1]

    elf1_start, elf1_end = elf1.split("-")
    elf2_start, elf2_end = elf2.split("-")
    
    elf1_start, elf1_end = int(elf1_start), int(elf1_end)
    elf2_start, elf2_end = int(elf2_start), int(elf2_end)
    
    if (elf1_start <= elf2_start and elf1_end >= elf2_end) or (elf2_start <= elf1_start and elf2_end >= elf1_end):
        overlap_count += 1
        partial_overlap_count += 1
    elif ((elf1_start <= elf2_start and elf1_end >= elf2_start) 
          or (elf2_end <= elf1_start and elf2_end >= elf1_start)
          or  (elf1_start >= elf2_start and elf1_start <= elf2_end) 
          or (elf2_start >= elf1_start and elf2_start <= elf1_end)
          ):
        partial_overlap_count += 1
        
    
        
        

expanded_rotas_str = [[expand_ranges(rota) for rota in elf] for elf in split_by_comma]

expanded_rotas = [[[int(room) for room in rota.split(",")] for rota in elves] for elves in expanded_rotas_str]


rota_pdf = pd.DataFrame(split_by_comma, columns=['elf1', 'elf2'])

rota_pdf['elf1'] = rota_pdf['elf1'].map(expand_ranges)
rota_pdf['elf2'] = rota_pdf['elf2'].map(expand_ranges)

rota_list = rota_pdf.values.tolist()
rota_list_split = [rota_list.split(",") for rota in rota_list]

