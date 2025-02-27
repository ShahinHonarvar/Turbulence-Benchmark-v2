def sum_in_range(numbers):
    total = 0
    for n in numbers:
        if 10 <= n <= 79:
            total += n
    return total