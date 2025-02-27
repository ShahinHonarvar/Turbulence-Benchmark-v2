def all_even_ints_exclusive(lst):
    result = []
    for i, num in enumerate(lst):
        if 20 <= i < 51 and num % 2 == 0:
            result.append(num)
    return result