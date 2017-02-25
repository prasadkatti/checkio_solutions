
"""
Link to the problem statement
https://py.checkio.org/mission/radiation-search/
"""


from collections import defaultdict
​
​
def part_locs(container):
​
    locations = defaultdict(list)
    for row_id, row in enumerate(container):
        for col_id, spare_part in enumerate(row):
            locations[spare_part].append((row_id, col_id))
    print locations
    return locations
​
​
def adjacents(coordinates):
​
    x, y = coordinates
    neighbors = []
    neighbors.append((x, y - 1))
    neighbors.append((x, y + 1))
    neighbors.append((x + 1, y))
    neighbors.append((x - 1, y))
    return neighbors
​
​
def merge_groups(list1, list2):
    for x in list1:
        for y in list2:
            if y in adjacents(x):
                list1.extend(list2)
                while list2:
                    list2.pop()
                return True
​
​
def form_groups(coordinates):
​
    groups = [[i] for i in coordinates]
    while True:
        new_associations = False
        for i in groups:
            for j in groups:
                if i is j:
                    continue
                changed = merge_groups(i, j)
                if changed:
                    new_associations = True
                    break
        groups = [i for i in groups if i]
        if not new_associations:
            break
    return groups
​
​
def unionize(locations):
​
    final_groups = {}
    for i in range(6):
        final_groups[i] = form_groups(locations[i])
    return final_groups
​
def checkio(container):
​
    unions = unionize(part_locs(container))
    print unions
    spare_part = None
    length = 0
    for k, v in unions.items():
        if v:
            longest_for_k = max([len(i) for i in v])
            if longest_for_k > length:
                spare_part = k
                length = longest_for_k
    return [length, spare_part]
