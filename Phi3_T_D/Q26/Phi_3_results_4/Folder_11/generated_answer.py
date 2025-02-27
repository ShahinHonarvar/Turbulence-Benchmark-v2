def sum_in_range(lst):
    result = 0
    for num in lst:
        if 11 <= num <= 76:
            result += num
    return result