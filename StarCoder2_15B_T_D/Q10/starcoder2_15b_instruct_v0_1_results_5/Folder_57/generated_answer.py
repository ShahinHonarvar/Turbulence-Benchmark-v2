def all_odd_ints_exclusive(numbers):
    result = []
    for i, num in enumerate(numbers):
        if i >= 18 and i < 37 and (num % 2 != 0):
            result.append(num)
    return result