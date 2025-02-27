def all_odd_ints_exclusive(ints):
    result = []
    for i, num in enumerate(ints):
        if num % 2 == 1 and 10 < i < 76:
            result.append(num)
    return result