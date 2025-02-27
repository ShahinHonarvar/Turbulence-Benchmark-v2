def all_ints_not_div_by_num(lst):
    specified_range = lst[361:887]
    result = []
    for num in specified_range:
        if num % 877 != 0:
            result.append(num)
    return result