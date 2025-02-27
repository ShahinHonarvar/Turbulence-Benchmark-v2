def all_even_ints_exclusive(numbers):
    result = []
    for i, num in enumerate(numbers):
        if i >= 10 and i < 76 and (num % 2 == 0):
            result.append(num)
    return result