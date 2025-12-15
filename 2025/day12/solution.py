import re

def get_data():
    shapes = dict()
    sections = []
    with open("input.txt") as f:
        for line in f:
            if re.match(r"^[0-9]+:", line):
                current_key = int(line.strip()[:-1])
                shapes[current_key] = {"shape": [], "area": 0}
            elif line.startswith(".") or line.startswith("#"):
                shapes[current_key]["shape"].append([0 if c == "." else 1 for c in line.strip()])
                shapes[current_key]["area"] += sum(shapes[current_key]["shape"][-1])
            elif not line.strip():
                continue
            else:
                supp = dict()
                parts = line.strip().split(":")
                w, h = map(int, parts[0].split("x"))
                supp["w"] = w
                supp["h"] = h
                supp["presents"] = {i:int(pid) for i, pid in enumerate(parts[1].strip().split())}
                sections.append(supp)
    return shapes, sections

def check_fitting(section, shapes): # Only works in this case, not generalized! (area_presents <= area coulld not fit!)
    w, h = section["w"], section["h"]
    area = w * h
    area_presents = 0
    for k in section["presents"].keys():
        area_presents += shapes[k]["area"]*section["presents"][k]
    if area_presents > area:
        return 0
    return 1

def main():
    shapes, sections = get_data()  
    fittings = list(map(lambda x: check_fitting(x, shapes), sections))
    print(f"Number of the regions that can fit the presents: {sum(fittings)}")

if __name__ == "__main__":
    main()