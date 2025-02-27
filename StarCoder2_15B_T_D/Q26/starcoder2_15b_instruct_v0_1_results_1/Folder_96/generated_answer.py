def sum_in_range(numbers):
    total = 0
    for n in numbers:
        if 4 <= n <= 8:
            total += n
    return total