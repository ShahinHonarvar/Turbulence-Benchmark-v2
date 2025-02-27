def sum_even_ints_inclusive(numbers):
    total = 0
    for i, num in enumerate(numbers):
        if i >= 27 and i <= 55 and (num % 2 == 0):
            total += num
    return total