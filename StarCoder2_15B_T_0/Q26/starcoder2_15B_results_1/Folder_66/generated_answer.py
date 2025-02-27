def sum_in_range(numbers):
    total = 0
    for num in numbers:
        if 28 <= num <= 96:
            total += num
    return total