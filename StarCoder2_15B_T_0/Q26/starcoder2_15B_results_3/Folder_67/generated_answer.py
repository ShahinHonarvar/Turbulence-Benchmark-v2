def sum_in_range(numbers):
    total = 0
    for num in numbers:
        if 31 <= num <= 50:
            total += num
    return total