def all_odd_ints_inclusive(ints):
    result = []
    for i, num in enumerate(ints):
        if i >= 31 and i <= 72 and (num % 2 == 1):
            result.append(num)
    return result