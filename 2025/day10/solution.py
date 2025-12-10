from itertools import combinations_with_replacement

def get_manuals():
    manuals = []
    with open("input.txt") as f:
        for line in f:
            manual = dict()
            supp = line.strip().split()
            manual["light_diagram"] = [0 if light == '.' else 1 for light in supp[0][1:-1]]
            manual["joltages"] = [int(joltage) for joltage in supp[-1][1:-1].split(",")]
            manual["buttons"] = [[int(action) for action in button[1:-1].split(",")] for button in supp[1:-1]]
            manuals.append(manual)
    return manuals

def get_buttons(buttons, n):
    if n == 1:
        return buttons
    else:
        new_buttons = []
        for comb in list(combinations_with_replacement(range(len(buttons)), n)):
            supp = []
            for i in comb:
                supp += buttons[i]
            new_buttons.append(supp)
        return new_buttons

def check_lists(l1, l2):
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            return False
    return True

def check_configuration(manual, n):
    buttons = get_buttons(manual["buttons"], n)
    desiderata = manual["light_diagram"]
    for button in buttons:
        support = [0]*len(desiderata)
        for light in button:
            support[light] += 1
        support = [s % 2 for s in support]
        if check_lists(desiderata, support):
            return True
    return False

def check_configuration_with_joltages(manual, n):
    buttons = get_buttons(manual["buttons"], n)
    joltages = manual["joltages"]
    for button in buttons:
        support = [0]*len(joltages)
        for light in button:
            support[light] += 1
            if check_lists(joltages, support):
                return True
    return False

def configure_machine(manual, joltages):
    steps = 1
    if joltages:
        while True:
            if check_configuration_with_joltages(manual, steps):
                print("ok")
                return steps
            steps += 1
    else:
        while True:
            if check_configuration(manual, steps):
                return steps
            steps += 1

def main():
    manuals = get_manuals()
    total_steps = sum(map(lambda m: configure_machine(m, False), manuals))
    print(f"Total steps to configure all machines: {total_steps}")
    total_steps_with_joltages = sum(map(lambda m: configure_machine(m, True), manuals))
    print(f"Total steps to configure all machines with joltages: {total_steps_with_joltages}")

if __name__ == "__main__":
    main()