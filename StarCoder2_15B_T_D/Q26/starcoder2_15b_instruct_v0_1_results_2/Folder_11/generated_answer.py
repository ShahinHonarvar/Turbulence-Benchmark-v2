def sum_in_range(numbers):
    total = 0
    for n in numbers:
        if 11 <= n <= 76:
            total += n
    return total