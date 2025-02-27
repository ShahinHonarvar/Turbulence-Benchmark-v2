def sum_even_ints_inclusive(numbers):
    sum_even = 0
    for index in range(40, 42):
        if index < len(numbers) and numbers[index] % 2 == 0:
            sum_even += numbers[index]
    return sum_even