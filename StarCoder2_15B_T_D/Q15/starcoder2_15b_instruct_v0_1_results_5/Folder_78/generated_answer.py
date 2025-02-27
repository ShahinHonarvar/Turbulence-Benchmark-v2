def sum_odd_ints_inclusive(numbers):
    sum = 0
    for number in numbers[43:52]:
        if number % 2 != 0:
            sum += number
    return sum