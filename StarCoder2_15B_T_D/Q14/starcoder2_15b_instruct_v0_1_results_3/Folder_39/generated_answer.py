def find_second_smallest_num(numbers):
    sorted_sublist = sorted(numbers[28:41])
    if len(sorted_sublist) >= 2:
        return sorted_sublist[1]
    else:
        return None