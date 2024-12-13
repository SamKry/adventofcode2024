import numpy as np
import array
from pprint import pprint
from utils import char2Array
from utils import int2Array
import re

import math

from scipy.optimize import linprog



dafaFile = "13/data.txt"
# dafaFile = "13/data_small.txt"


"""
example:

Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""

def solve_machine_linear(X_A, Y_A, X_B, Y_B, X, Y):
    bound = [(0, None), (0, None)]

    f = [3, 1]

    A_eq = [[X_A, X_B], [Y_A, Y_B]]
    B_eq = [X, Y]

    sol = linprog(f, A_eq=A_eq, b_eq=B_eq, bounds=bound).fun

    if sol == np.inf:
        return None
    
    if sol == None:
        return None
    
    if not math.isclose(sol, round(sol), rel_tol=1e-6):
        print("Wrong ones: ", sol)
        return None
    
    sol = round(sol)

    print(f"Machine: ({X_A}, {Y_A}) ({X_B}, {Y_B}) - {X}, {Y})\tSolution: {sol}")
    return sol


def solve_all_machines_brute_force(machines):
    total_tokens = 0
    total_prizes = 0

    for machine in machines:
        solution = solve_machine_linear(*machine)
        if solution is not None:
            total_prizes += 1
            total_tokens += solution

    return total_prizes, total_tokens



def parse_input(file_path):
    machines = []  # List to hold machine data
    
    with open(file_path, 'r') as file:
        data = file.read().strip()
    
    # Split the data into groups (each machine block)
    machine_blocks = data.split("\n\n")
    
    for block in machine_blocks:
        lines = block.split("\n")
        
        # Extract coefficients for A and B buttons
        a_match = re.search(r"Button A: X\+(\d+), Y\+(\d+)", lines[0])
        b_match = re.search(r"Button B: X\+(\d+), Y\+(\d+)", lines[1])
        
        # Extract prize coordinates
        prize_match = re.search(r"Prize: X=(\d+), Y=(\d+)", lines[2])
        
        if a_match and b_match and prize_match:
            x_a, y_a = map(int, a_match.groups())
            x_b, y_b = map(int, b_match.groups())
            x_prize, y_prize = map(int, prize_match.groups())

            x_prize = x_prize + 10000000000000
            y_prize = y_prize + 10000000000000
            
            # Add machine data as a tuple
            machines.append((x_a, y_a, x_b, y_b, x_prize, y_prize))
    
    return machines


machines = parse_input(dafaFile)

# pprint(machines)


total_prizes, total_tokens = solve_all_machines_brute_force(machines)
# print(f"Total Prizes: {total_prizes}, Total Tokens: {total_tokens}") # !!!! this is the wrong answer

# 935192588115276421 not right

# 159950986978526 too high