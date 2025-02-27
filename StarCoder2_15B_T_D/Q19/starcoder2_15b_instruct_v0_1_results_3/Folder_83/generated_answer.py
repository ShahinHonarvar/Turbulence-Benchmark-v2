def all_ints_not_div_by_num(ints):
    output = []
    for i, num in enumerate(ints):
        if i >= 90 and i < 200 and (num % -31 != 0):
            output.append(num)
    return output