def all_ints_div_by_num(ints):
    divisible = []
    for i, num in enumerate(ints):
        if i >= 57 and i <= 67 and (num % 90 == 0):
            divisible.append(num)
    return divisible