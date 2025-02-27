def sum_in_range(numbers):
    total = 0
    for num in numbers:
        if 3 <= num <= 9:
            total += num
    return total