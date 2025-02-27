def all_ints_div_by_num(integers):
    result = []
    for i, num in enumerate(integers):
        if i >= 70 and i <= 76 and (num % -92 == 0):
            result.append(num)
    return result