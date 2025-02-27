def sum_even_ints_inclusive(numbers):
    sum_even = 0
    for i in range(40, 42):
        if i < len(numbers) and numbers[i] % 2 == 0:
            sum_even += numbers[i]
    return sum_even