def all_even_ints_exclusive(ints):
    result = []
    for i, num in enumerate(ints):
        if num % 2 == 0 and 598 < i < 767:
            result.append(num)
    return result