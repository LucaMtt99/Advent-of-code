def get_tiles():
    with open("input.txt") as f:
        tiles = [list(map(int, line.strip().split(","))) for line in f.readlines()]
    return tiles

def get_biggest_rectangle(tiles):
    biggest_area = 0
    for j,tile in enumerate(tiles):
        for i,other_tile in enumerate(tiles):
            if i > j:
                area = (abs(tile[0] - other_tile[0]) + 1) * (abs(tile[1] - other_tile[1]) + 1)
                if area > biggest_area:
                    biggest_area = area
    return biggest_area

def ccw(A, B, C):
    return (C[1]-A[1]) * (B[0]-A[0]) - (B[1]-A[1]) * (C[0]-A[0])

def intersect(A, B, C, D):
    return ccw(A,B,C) * ccw(A,B,D) < 0 and ccw(C,D,A) * ccw(C,D,B) < 0

def is_point_in_polygon(point, polygon):
    x, y = point
    n = len(polygon)
    inside = False
    p1x, p1y = polygon[0]
    for i in range(n + 1):
        p2x, p2y = polygon[i % n]
        if (min(p1x, p2x) <= x <= max(p1x, p2x)) and (min(p1y, p2y) <= y <= max(p1y, p2y)) and \
           (y - p1y) * (p2x - p1x) == (p2y - p1y) * (x - p1x):
            return True  
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside

def is_rect_valid(p1, p2, polygon):
    c1 = [p1[0], p2[1]]
    c2 = [p2[0], p1[1]]
    if not is_point_in_polygon(c1, polygon) or not is_point_in_polygon(c2, polygon):
        return False
    rect_edges = [(p1, c1), (c1, p2), (p2, c2), (c2, p1)]
    n = len(polygon)
    for i in range(n):
        poly_p1 = polygon[i]
        poly_p2 = polygon[(i + 1) % n]
        for r_start, r_end in rect_edges:
            if intersect(poly_p1, poly_p2, r_start, r_end):
                return False         
    return True

def get_biggest_rectangle_ruled(tiles):
    candidates = []
    for j, tile in enumerate(tiles):
        for i, other_tile in enumerate(tiles):
            if i > j:
                area = (abs(tile[0] - other_tile[0]) + 1) * (abs(tile[1] - other_tile[1]) + 1)
                candidates.append((area, tile, other_tile))
    candidates.sort(key=lambda x: x[0], reverse=True)
    for area, p1, p2 in candidates:
        if is_rect_valid(p1, p2, tiles):
            return area

def main():
    tiles = get_tiles()
    biggest_area = get_biggest_rectangle(tiles)
    print("Biggest rectangle area:", biggest_area)
    biggest_area_ruled = get_biggest_rectangle_ruled(tiles)
    print("Biggest rectangle area with rules:", biggest_area_ruled)

if __name__ == "__main__":
    main()