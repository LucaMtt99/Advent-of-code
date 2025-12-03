def get_banks   ():
    with open("input.txt") as f:
        lines = f.readlines()
    banks = [[int(x) for x in line.strip()] for line in lines]
    return banks

def get_max_joltage(bank):
    max_value = max(bank)
    max_value_index = bank.index(max_value)
    if max_value_index == len(bank) - 1:
        return 10*(max(bank[:-1])) + max_value
    else:
        return 10*max_value + max(bank[max_value_index+1:])

def get_max_joltage(bank, n_batteries):
    if n_batteries == 1:
        return max(bank)
    if len(bank) <= n_batteries:
        return int("".join(map(str, bank)))
    max_joltage = 0
    max_value = max(bank[:-n_batteries+1])
    max_value_index = bank.index(max_value)
    if max_value_index == len(bank) - n_batteries:
        return int("".join(map(str, bank[-n_batteries:])))
    else:
        max_joltage += get_max_joltage(bank[max_value_index+1:], n_batteries-1)
    return (10**(n_batteries-1))*max_value + max_joltage

def get_output_joltage(banks, n_batteries):
    output_joltage = sum(list(map(lambda bank: get_max_joltage(bank, n_batteries=n_batteries), banks)))
    return output_joltage

def main():
    banks = get_banks()
    output_joltage_2 = get_output_joltage(banks, n_batteries=2)
    output_joltage_12 = get_output_joltage(banks, n_batteries=12)
    print("Output Joltage (2 batteries):", output_joltage_2)
    print("Output Joltage (12 batteries):", output_joltage_12)

if __name__ == "__main__":
    main()