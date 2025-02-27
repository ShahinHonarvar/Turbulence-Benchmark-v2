def sum_in_range(numbers):
    total = 0
    for num in numbers:
        if 13 <= num <= 35:
            total += num
    return total