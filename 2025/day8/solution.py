from scipy.cluster.hierarchy import  linkage
import numpy as np

def get_boxes():
    boxes = []
    with open("input.txt") as f:
        for line in f:
            boxes.append(list(map(int, line.split(","))))
    return boxes

def main():
    boxes = get_boxes()
    linkage_matrix = linkage(boxes)
    product_of_sizes = ...
    print(f"Product of top 3 clusters' size: {product_of_sizes}")

if __name__ == "__main__":
    main()