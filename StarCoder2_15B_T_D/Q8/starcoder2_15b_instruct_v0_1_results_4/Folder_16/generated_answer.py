def all_even_ints_exclusive(int_list):
    result = []
    for i, num in enumerate(int_list):
        if i >= 86 and i < 90 and (num % 2 == 0):
            result.append(num)
    return result