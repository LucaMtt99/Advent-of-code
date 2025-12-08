from scipy.spatial import distance_matrix
import numpy as np

def get_boxes():
    boxes = []
    with open("input.txt") as f:
        for line in f:
            boxes.append(list(map(int, line.split(","))))
    return boxes

def main():
    boxes = get_boxes()
    distances = distance_matrix(boxes, boxes)
    print(distances)
    product_of_sizes = ...
    print(f"Product of top 3 clusters' size: {product_of_sizes}")

if __name__ == "__main__":
    main()