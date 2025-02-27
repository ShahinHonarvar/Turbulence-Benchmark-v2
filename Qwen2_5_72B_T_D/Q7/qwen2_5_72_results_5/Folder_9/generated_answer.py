def all_even_ints_inclusive(numbers):
    result = []
    for index in range(73, 74):
        if numbers[index] % 2 == 0:
            result.append(numbers[index])
    return result