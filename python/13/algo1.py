import numpy as np
import array
from pprint import pprint
from utils import char2Array
from utils import int2Array
import re


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

def solve_machine_brute_force(X_A, Y_A, X_B, Y_B, X, Y):
    min_cost = float('inf')  # Initialize with an impossibly high value
    found_solution = False


    # Iterate through all possible combinations of a and b (button presses)
    for a in range(101):  # Presses for button A (0 to 100)
        for b in range(101):  # Presses for button B (0 to 100)
            # Calculate the resulting X and Y coordinates
            current_x = a * X_A + b * X_B
            current_y = a * Y_A + b * Y_B

            # Check if the current combination reaches the prize location
            if current_x == X and current_y == Y:
                found_solution = True
                cost = 3 * a + b  # Calculate the cost (3 tokens for A, 1 token for B)
                min_cost = min(min_cost, cost)  # Track the minimum cost

    # If no solution found, return None
    if not found_solution:
        return None
    return min_cost


def solve_all_machines_brute_force(machines):
    total_tokens = 0
    total_prizes = 0

    for machine in machines:
        solution = solve_machine_brute_force(*machine)
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
            
            # Add machine data as a tuple
            machines.append((x_a, y_a, x_b, y_b, x_prize, y_prize))
    
    return machines


machines = parse_input(dafaFile)

# pprint(machines)


total_prizes, total_tokens = solve_all_machines_brute_force(machines)
print(f"Total Prizes: {total_prizes}, Total Tokens: {total_tokens}")