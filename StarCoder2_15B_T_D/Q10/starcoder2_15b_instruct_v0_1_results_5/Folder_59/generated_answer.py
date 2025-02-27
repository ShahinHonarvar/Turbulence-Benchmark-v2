def all_odd_ints_exclusive(ints):
    result = []
    for i, num in enumerate(ints):
        if i >= 0 and i < 9 and (num % 2 == 1):
            result.append(num)
    return result