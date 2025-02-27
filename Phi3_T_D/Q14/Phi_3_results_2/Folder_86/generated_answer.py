def find_second_smallest_num(lst):
    specific_range = lst[33:37]
    if len(set(specific_range)) < 2:
        return None
    second_smallest = sorted(set(specific_range))[1]
    return second_smallest