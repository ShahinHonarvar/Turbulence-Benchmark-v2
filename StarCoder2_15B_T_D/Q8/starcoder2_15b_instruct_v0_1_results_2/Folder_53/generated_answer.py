def all_even_ints_exclusive(ints):
    result = []
    for i, num in enumerate(ints):
        if i >= 100 and i < 102 and (num % 2 == 0):
            result.append(num)
    return result