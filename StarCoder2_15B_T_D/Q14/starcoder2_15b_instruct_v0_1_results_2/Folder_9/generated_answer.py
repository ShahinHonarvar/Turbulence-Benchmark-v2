def find_second_smallest_num(lst):
    subset = sorted(lst[70:201])
    if len(subset) >= 2:
        return subset[1]
    else:
        return None