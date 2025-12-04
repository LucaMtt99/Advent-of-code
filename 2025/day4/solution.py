import numpy as np
from scipy.signal import convolve2d

def get_roll_matrix():
    with open("input.txt") as f:
        lines = f.readlines()
    roll_matrix = [[1 if x=="@" else 0 for x in line.strip()] for line in lines]
    return np.array(roll_matrix)
    
def get_accesible_rolls(roll_matrix):
    kernel = np.array([[-1, -1, -1],
                       [-1,  4, -1],
                       [-1, -1, -1]])
    convolved = convolve2d(roll_matrix, kernel, mode='same', boundary='fill', fillvalue=0)
    accesible_rolls = np.clip(convolved, 0, 1)
    return accesible_rolls

def remove_max_number_of_rolls(roll_matrix):
    removed = list()
    while True:
        accesible_rolls = get_accesible_rolls(roll_matrix)
        if accesible_rolls.sum() == 0:
            break
        else:
            roll_matrix = roll_matrix - accesible_rolls
            removed.append(accesible_rolls.sum())
    return sum(removed)

def main():
    roll_matrix = get_roll_matrix()
    accesible_rolls = get_accesible_rolls(roll_matrix)
    print("Number of accessible rolls at iter 1:", accesible_rolls.sum())
    print("Total number of removed rolls:", remove_max_number_of_rolls(roll_matrix))

if __name__ == "__main__":
    main()