def all_odd_ints_exclusive(ints):
    result = []
    for i, num in enumerate(ints):
        if i >= 56 and i < 92 and (num % 2 == 1):
            result.append(num)
    return result