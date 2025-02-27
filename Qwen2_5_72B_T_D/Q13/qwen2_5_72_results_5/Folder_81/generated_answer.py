def find_second_largest_num(numbers):
    sublist = numbers[10:101]
    if len(sublist) < 2:
        return None
    max_num = max(sublist)
    second_max = None
    for num in sublist:
        if num > second_max and num < max_num:
            second_max = num
    return second_max