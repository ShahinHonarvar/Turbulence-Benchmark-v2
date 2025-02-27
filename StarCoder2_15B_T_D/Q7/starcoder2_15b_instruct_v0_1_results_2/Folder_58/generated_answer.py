def all_even_ints_inclusive(numbers):
    result = []
    for i, num in enumerate(numbers):
        if i >= 209 and i <= 556 and (num % 2 == 0):
            result.append(num)
    return result