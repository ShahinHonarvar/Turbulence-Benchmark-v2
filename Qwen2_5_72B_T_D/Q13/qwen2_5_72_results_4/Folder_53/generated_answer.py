def find_second_largest_num(numbers):
    sublist = numbers[100:201]
    if len(sublist) < 2:
        return None
    max_num = max(sublist)
    second_max = None
    for num in sublist:
        if num != max_num:
            if second_max is None or num > second_max:
                second_max = num
    return second_max