def sum_in_range(numbers):
    total = 0
    for num in numbers:
        if -100 <= num <= -55:
            total += num
    return total