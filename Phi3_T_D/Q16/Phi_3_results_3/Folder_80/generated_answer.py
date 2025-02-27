def sum_even_ints_inclusive(numbers):
    even_sum = 0
    if len(numbers) > 66 and numbers[64] % 2 == 0:
        even_sum += numbers[64]
    if len(numbers) > 65 and numbers[65] % 2 == 0:
        even_sum += numbers[65]
    if len(numbers) > 66 and numbers[66] % 2 == 0:
        even_sum += numbers[66]
    return even_sum