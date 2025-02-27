def all_even_ints_inclusive(ints):
    result = []
    for i, num in enumerate(ints):
        if i >= 32 and i <= 35 and (num % 2 == 0):
            result.append(num)
    return result