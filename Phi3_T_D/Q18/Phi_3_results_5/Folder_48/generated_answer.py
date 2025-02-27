def sum_ints_div_by_either_nums(lst):
    start, end = (306, 957)
    threshold = 1051
    return sum((num for index, num in enumerate(lst[start:end + 1], start) if num % 982 == 0 or num % 319 == 0))