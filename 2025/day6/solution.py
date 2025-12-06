import pandas as pd
import numpy as np

def get_data_1():
    data = []
    with open("input.txt") as f:
        for line in f:
            entries = line.split()
            entries = [e.strip() for e in entries if e]
            data.append(entries)
    df = pd.DataFrame(data).T
    df.iloc[:,:-1] = df.iloc[:,:-1].astype(int)
    return df

def get_data_2():
    data = []
    with open("input.txt") as f:
        lines = f.readlines()
    lines = [line[::-1].replace("\n", "") for line in lines]
    operands = lines[-1].split()
    operands = [operand.strip() for operand in operands if operand]
    lines = lines[:-1]
    max_len = 0
    for line in lines: 
        if len(line) > max_len:
            max_len=len(line) 
    lines = [line + " " *(max_len-len(line)) for line in lines]
    operation = []
    for i in range(max_len):
        number = ""
        for j in range(len(lines)):
            if lines[j][i] != " ":
                number += lines[j][i]
        if number:
            operation.append(int(number))
        else:
            data.append(operation)
            operation = []
    data.append(operation)
    df = pd.DataFrame(data)
    df["operand"] = operands
    return df

def calculate(x):
    if x.iloc[-1] == "+":
        return x[:-1].sum()
    else:
        return x[:-1].prod()
    
def main():
    df_1 = get_data_1()
    df_2 = get_data_2()
    sum_problems_1 = df_1.apply(calculate, axis=1).sum()
    sum_problems_2 = df_2.apply(calculate, axis=1).sum()
    print(f"sum of results challenge 1: {sum_problems_1}")
    print(f"sum of results challenge 2: {sum_problems_2}")

if __name__ == "__main__":
    main()