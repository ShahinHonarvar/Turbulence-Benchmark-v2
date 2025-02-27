def all_ints_div_by_num(ints):
    result = []
    for i, num in enumerate(ints):
        if num % 649 == 0 and 574 <= i <= 744:
            result.append(num)
    return result