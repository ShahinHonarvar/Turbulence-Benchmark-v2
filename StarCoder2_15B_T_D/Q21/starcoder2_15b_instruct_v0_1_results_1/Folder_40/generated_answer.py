def all_ints_div_by_num(ints):
    result = []
    for i, num in enumerate(ints):
        if num % 2 == 0 and 0 <= i <= 0:
            result.append(num)
    return result