def get_diagram():
    with open("input.txt") as f:
        lines = f.readlines()
    lines = [list(line.replace("\n", "")) for line in lines]
    return lines

def new_paths(line, beam):
    if (line[(beam+2)] == "^" and (beam+2) < len(line)) and (line[(beam-2)] == "^" and (beam-2) >= 0):
        return 2
    elif (line[(beam+2)] == "^" and (beam+2) < len(line)) or ((beam-2) == "^" and (beam-2) >= 0):
        return 1
    else:
        return 1

def walk(diagram):
    diagram_w = len(diagram[0])
    split_count = 0
    beams = set()
    beams.add(diagram[0].index("S"))
    for line in diagram[1:-1]:
        for beam in list(beams):
            if line[beam] == "^":
                split_count += 1
                beams.remove(beam)
                if (beam+1) < diagram_w:
                    beams.add(beam+1)
                if (beam-1) >= 0: 
                    beams.add(beam-1)
    return split_count

def main():
    diagram = get_diagram()
    split_count = walk(diagram)
    print(f"Number of splits: {split_count}")
    def timelines(start, depth):
        if depth == len(diagram): return 1
        if not isinstance(diagram[depth][start], int):
            diagram[depth][start] = timelines(start, depth + 1) if diagram[depth][start] == '.' else timelines(start - 1, depth + 1) + timelines(start + 1, depth + 1)
        return diagram[depth][start]
    paths_count = timelines(diagram[0].index('S'), 1)
    print(f"Number of paths: {paths_count}")

if __name__ == "__main__":
    main()