def get_ranges():
    with open("input.txt") as f:
        text = f.read()
    ranges = text.split(",")
    return ranges

divisors_cache = {}
def get_divisors(length):
    if length in divisors_cache:
        return divisors_cache[length]
    divisors = [length]
    for i in range(2, length//2+1):
        if not length%i:
            divisors.append(i)
    divisors_cache[length] = divisors
    return divisors

def check_invalid(id_code):
    code_length = len(id_code)
    divisors = get_divisors(code_length)
    print(f"Checking ID code: {id_code} with divisors: {divisors}")
    for divisor in divisors:
        check = True
        chunk_len = code_length // divisor
        base_pattern = id_code[0:chunk_len]
        for i in range(1,divisor):
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