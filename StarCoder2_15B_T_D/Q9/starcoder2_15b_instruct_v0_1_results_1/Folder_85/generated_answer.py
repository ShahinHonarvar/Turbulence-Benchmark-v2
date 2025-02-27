def all_odd_ints_inclusive(ints):
    result = []
    for i, num in enumerate(ints):
        if i >= 6 and i <= 8 and (num % 2 == 1):
            result.append(num)
    return result