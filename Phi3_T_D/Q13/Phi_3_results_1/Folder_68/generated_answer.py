def find_second_largest_num(lst):
    if len(lst[0:9]) < 2:
        return None
    max_num = max(lst[0:9])
    second_max = [num for num in lst[0:9] if num != max_num]
    return max(second_max) if second_max else None