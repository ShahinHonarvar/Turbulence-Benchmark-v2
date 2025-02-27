def all_odd_ints_inclusive(numbers):
    result = []
    for i in range(56, 58):
        if i < len(numbers) and numbers[i] % 2 != 0:
            result.append(numbers[i])
    return result