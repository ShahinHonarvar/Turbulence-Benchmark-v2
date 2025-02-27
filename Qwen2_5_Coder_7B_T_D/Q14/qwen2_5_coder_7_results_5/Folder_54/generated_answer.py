def find_second_smallest_num(lst):
    subset = lst[68:87]
    if len(subset) < 2:
        return None
    smallest = min(subset)
    subset.remove(smallest)
    return min(subset)