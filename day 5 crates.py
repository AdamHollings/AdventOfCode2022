# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 13:36:01 2022

Day 5 advent of code 2022

Copied solution from here: 
    
    https://github.com/Se7enSquared/AdventOfCode/blob/main/solutions_2022/solutions/day5.py?fbclid=IwAR0otXmton0AUzZHSw2gCVo-69lNVi8ZvZUuPx8Ta0X7KH2eoV_BSfr2UGE

@author: adho3
"""
from collections import namedtuple
from itertools import zip_longest
from pathlib import Path
import os
from typing import List

print(os.getcwd())

strategy_data = open("day_5_input.txt", "r").readlines()

CRATE_SIZE = 4
OFFSET = 1
PARTS = (1, 2)

def cleanup_stacks(stack_input: List[List[str]]) -> List[List[str]]:
    """a rather ridiculous way to clean and transpose the stacks"""
    new_stack = []
    for line in stack_input:
        l = [line[i : i + CRATE_SIZE] for i in range(0, len(line), CRATE_SIZE)]
        new_stack.append(l)
    transposed_stack = list(map(list, zip_longest(*new_stack, fillvalue="")))
    clean_stack = clean_list_items(transposed_stack)
    return [lst[::-1] for lst in clean_stack]


def clean_list_items(transposed_stack: List[List[str]]) -> List[List[str]]:
    """remove extraneous characters from list items"""
    stack_container = []
    chars_to_replace = ['[', ']', ' ', '\n']
    for l in transposed_stack:
        clean_letters = []
        for i in l:
            for char in chars_to_replace:
                i = i.replace(char, "")
            clean_letters.append(i)
        stack_container.append(clean_letters)
    return [[x for x in lst if x] for lst in stack_container]


def parse_instructions(instruction_line: str) -> namedtuple:
    """build a namedtuple of instructions"""
    Instruction = namedtuple("Instruction", "qty move_from move_to")
    quantity = int(instruction_line[1])
    move_from = int(instruction_line[3]) - OFFSET
    move_to = int(instruction_line[-1]) - OFFSET
    return Instruction(quantity, move_from, move_to)


def follow_instruction(stack: List[List[str]], instruction: namedtuple, part: int) -> List[List[str]]:
    """perform the actions in the instruction object"""
    items = stack[instruction.move_from][-instruction.qty :]
    if part == 1:
        items.reverse()
    new_list = stack[instruction.move_from][: -instruction.qty]
    stack[instruction.move_from] = new_list
    stack[instruction.move_to].extend(items)
    return stack


def execute_part(part: int, stack: List[List[str]]):
    """ execute based on day 5 part 1 or 2 """
    for line in instruction_lines:
        instruction_line = line.split()
        instruction = parse_instructions(instruction_line)
        new_stack = follow_instruction(stack, instruction, part)
    final_string = "".join(i[-1] for i in stack)
    print(final_string)


if __name__ == "__main__":
    print(f'Advent of Code Day 5 https://adventofcode.com/2022/day/5')

    all_input = open("day_5_input.txt", "r").readlines()
    stacks = all_input[:8]
    instruction_lines = all_input[10:]
    for part in PARTS:
        new_stack = cleanup_stacks(stacks)
        execute_part(part, new_stack)

