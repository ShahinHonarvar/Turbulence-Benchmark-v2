def all_odd_ints_exclusive(numbers):
    result = []
    for i in range(101, 102):
        if numbers[i] % 2 != 0:
            result.append(numbers[i])
    return result