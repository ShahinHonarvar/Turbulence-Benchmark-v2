def find_second_largest_num(numbers):
    sublist = numbers[28:41]
    if len(sublist) < 2:
        return None
    max1, max2 = sorted(set(sublist), reverse=True)[:2]
    return max2