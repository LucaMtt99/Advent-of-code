def get_boxes():
    boxes = []
    with open("input.txt") as f:
        for line in f:
            boxes.append(list(map(int, line.split(","))))
    return boxes

def get_distances(boxes):
    distances = []
    for i,(x,y,z) in enumerate(boxes):
        for j,(x1,y1,z1) in enumerate(boxes):
            if i > j:
                dist = (x-x1)**2 + (y-y1)**2 + (z-z1)**2
                distances.append((dist, i, j))
    return sorted(distances, key=lambda x: x[0])

def add_to_clusters(clusters, parent, i, j):
    i_label = parent.get(i)
    j_label = parent.get(j)
    if not i_label and not j_label:
        c_label = max(clusters.keys(), default=0) + 1
        clusters[c_label] = set([i, j])
        parent[i] = c_label
        parent[j] = c_label
    elif i_label and not j_label:
        clusters[i_label].add(j)
        parent[j] = i_label
    elif not i_label and j_label:
        clusters[j_label].add(i)
        parent[i] = j_label
    elif i_label != j_label:
        clusters[i_label] = clusters[i_label].union(clusters[j_label])
        for node in clusters[j_label]:
            parent[node] = i_label
        del clusters[j_label]
        
def get_circuits(distances, n=1000):
    clusters = dict()
    parent = dict()
    for _, i, j in distances[:n]:
        add_to_clusters(clusters, parent, i, j)
    return clusters

def get_size_largest_circuits(circuits, top_k=3):
    sizes = sorted([len(circuits[label]) for label in circuits.keys()], reverse=True)
    return sizes[:top_k]  

def get_product(sizes):
    product = 1
    for size in sizes:
        product *= size
    return product

def get_last_connection(distances, n_boxes):
    clusters = dict()
    parent = dict()
    for _, i, j in distances:
        add_to_clusters(clusters, parent, i, j)
        if len(clusters)==1 and len(clusters[next(iter(clusters))])==n_boxes:
            return i,j

def main():
    boxes = get_boxes()
    distances = get_distances(boxes)
    circuits = get_circuits(distances)
    sizes = get_size_largest_circuits(circuits)
    product_of_sizes = get_product(sizes)
    print(f"Product of top 3 clusters' size: {product_of_sizes}")
    last_connection = get_last_connection(distances, len(boxes))
    last_connection_product = boxes[last_connection[0]][0] * boxes[last_connection[1]][0]
    print(f"Last connection made between boxes: {last_connection_product}")

if __name__ == "__main__":
    main()