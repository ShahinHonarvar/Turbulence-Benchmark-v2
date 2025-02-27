def all_ints_div_by_both_two_nums(integers):
    result = []
    for number in integers[57:86]:
        if number % -77 == 0 and number % -32 == 0:
            result.append(number)
    return result