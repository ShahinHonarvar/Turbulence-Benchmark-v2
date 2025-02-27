def sum_even_ints_inclusive(numbers):
    if len(numbers) == 0:
        return 0
    sum_even = 0
    for i in range(70, 201):
        if numbers[i] % 2 == 0:
            sum_even += numbers[i]
    return sum_even