def all_odd_ints_inclusive(numbers):
    result = []
    for index in range(56, 58):
        if index < len(numbers) and numbers[index] % 2 != 0:
            result.append(numbers[index])
    return result