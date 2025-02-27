def find_second_smallest_num(lst):
    start, end = (66, 93)
    valid_range = lst[start:end + 1]
    if len(valid_range) < 2:
        return None
    unique_nums = set(valid_range)
    if len(unique_nums) < 2:
        return None
    return sorted(unique_nums)[1]