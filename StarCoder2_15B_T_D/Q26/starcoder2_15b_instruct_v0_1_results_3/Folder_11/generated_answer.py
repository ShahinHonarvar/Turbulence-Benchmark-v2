def sum_in_range(numbers):
    total = 0
    for num in numbers:
        if 11 <= num <= 76:
            total += num
    return total