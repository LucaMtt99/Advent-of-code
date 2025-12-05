def get_data():
    fresh_products = []
    products_to_check = []
    with open("input.txt") as f:
        for line in f:
            if "-" in line:
                start,end = line.split("-")
                fresh_products.append((int(start.strip()), int(end.strip())))
            else:
                try:
                    products_to_check.append(int(line.strip()))
                except:
                    continue
    return fresh_products, products_to_check

def check_freshness(fresh_products, product_id):
    for start, end in fresh_products:
        if start <= product_id <= end:
            return True
    return False

def analyze_products(fresh_products, products_to_check):
    results = []
    for product_id in products_to_check:
        results.append(check_freshness(fresh_products, product_id))
    return sum(results)

def find_number_of_all_fresh_products(fresh_products):
    all_fresh = 0
    sorted_ranges = sorted(fresh_products, key=lambda x: x[0])
    current_start = sorted_ranges[0][0]
    current_end = sorted_ranges[0][1]
    for start, end in sorted_ranges[1:]:
        if start > current_end + 1:
            all_fresh += (current_end - current_start + 1)
            current_start = start
            current_end = end
        else:
            current_end = max(current_end, end)
    all_fresh += (current_end - current_start + 1)
    return all_fresh

def main():
    fresh_products, products_to_check = get_data()
    fresh_count = analyze_products(fresh_products, products_to_check)
    all_fresh = find_number_of_all_fresh_products(fresh_products)
    print(f"Number of fresh products: {fresh_count}")
    print(f"Number of all fresh product IDs: {all_fresh}")

if __name__ == "__main__":
    main()