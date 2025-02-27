def sum_odd_ints_inclusive(numbers):
    sum = 0
    for number in numbers[68:87]:
        if number % 2 != 0:
            sum += number
    return sum