def sum_in_range(numbers):
    total = 0
    for num in numbers:
        if -64 <= num <= 42:
            total += num
    return total