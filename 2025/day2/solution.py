def get_ranges():
    with open("input.txt") as f:
        text = f.read()
    ranges = text.split(",")
    return ranges

def get_dividers(length):
    dividers = [length]
    for i in range(2, length//2+1):
        if not length%i:
            dividers.append(i)
    return dividers

def check_invalid(id_code):
    code_length = len(id_code)
    dividers = get_dividers(code_length)
    print(f"Checking ID code: {id_code} with dividers: {dividers}")
    for divider in dividers:
        check = True
        chunk_len = code_length // divider
        base_pattern = id_code[0:chunk_len]
        for i in range(1,divider):
            if id_code[i*chunk_len:(i+1)*chunk_len] != base_pattern:
                check = False
                break
        if check:
            return True
    return False

def find_invalid_ids(ranges):
    invalid_ids = []
    for r in ranges:
        start, end = map(int, r.split("-"))
        for i in range(start, end + 1):
            id_code = str(i)
            if len(id_code) <= 1:
                continue
            if check_invalid(id_code):
                invalid_ids.append(i)
    return sum(invalid_ids), invalid_ids

def main():
    ranges = get_ranges()
    result, ids= find_invalid_ids(ranges)
    print(f"Invalid IDs: {ids}")
    print(f"Sum of invalid IDs: {result}")

if __name__ == "__main__":
    main()