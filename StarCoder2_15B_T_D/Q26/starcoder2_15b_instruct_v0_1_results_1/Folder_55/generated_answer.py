def sum_in_range(numbers):
    total = 0
    for n in numbers:
        if 3 <= n <= 6:
            total += n
    return total