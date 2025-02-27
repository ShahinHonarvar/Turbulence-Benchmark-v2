def sum_in_range(numbers):
    sum = 0
    for number in numbers:
        if number in range(-28, 574):
            sum += number
    return sum