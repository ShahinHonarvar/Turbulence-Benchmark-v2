def all_ints_div_by_num(lst):
    start, end, divisor = (315, 352, -858)
    result = [num for num in lst[start:end + 1] if num % divisor == 0]
    return result