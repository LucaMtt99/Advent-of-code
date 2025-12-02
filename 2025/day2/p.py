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
            if check_invalid(id_code):
                invalid_ids.append(i)
    return invalid_ids

print(find_invalid_ids(["998-1012"]))  # Example usage