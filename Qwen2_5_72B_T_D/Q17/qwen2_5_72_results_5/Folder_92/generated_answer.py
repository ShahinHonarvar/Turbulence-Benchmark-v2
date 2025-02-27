def all_ints_div_by_both_two_nums(lst):
    result = []
    if 0 <= 0 < len(lst):
        num = lst[0]
        if num % 1 == 0 and num % -1 == 0:
            result.append(num)
    return result