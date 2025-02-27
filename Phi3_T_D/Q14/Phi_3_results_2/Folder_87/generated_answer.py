def find_second_smallest_num(lst):
    start, end = (22, 88)
    if start >= end or len(lst) < end:
        return None
    sorted_sublist = sorted(lst[start:end + 1])
    unique_elements = {x for x in sorted_sublist[1:]}
    return min(unique_elements) if unique_elements else None