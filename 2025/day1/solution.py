def get_rotations():
    with open("input.txt") as f:
        lines = f.readlines()
    rotations = [int(line[1:]) if line.startswith("R") else -int(line[1:]) for line in lines]
    return rotations

def get_pwd(rotations):
    count_1 = 0
    count_2 = 0
    current_state = 50
    for rotation in rotations:
        if rotation < 0 and current_state == 0:
            current_state += 100
        current_state += rotation
        count_2 += (abs(current_state-50)+50)//100
        if not current_state%100:
            count_1+=1
        current_state %= 100
    return count_1, count_2

def main():
    rotations = get_rotations()
    pwd1, pwd2 = get_pwd(rotations)
    print("Password 1:", pwd1)
    print("Password 2:", pwd2)

if __name__ == "__main__":
    main()