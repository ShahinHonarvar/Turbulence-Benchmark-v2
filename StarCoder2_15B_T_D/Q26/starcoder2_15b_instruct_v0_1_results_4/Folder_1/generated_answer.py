def sum_in_range(numbers):

    def is_in_range(number):
        return number >= -97 and number <= -48
    sum = 0
    for number in numbers:
        if is_in_range(number):
            sum += number
    return sum