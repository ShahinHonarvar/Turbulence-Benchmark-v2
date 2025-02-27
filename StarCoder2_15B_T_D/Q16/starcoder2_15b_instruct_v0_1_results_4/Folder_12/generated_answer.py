def sum_even_ints_inclusive(numbers):
    total = 0
    for i, num in enumerate(numbers):
        if i >= 14 and i <= 64 and (num % 2 == 0):
            total += num
    return total