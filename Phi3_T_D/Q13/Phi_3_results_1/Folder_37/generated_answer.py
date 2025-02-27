def find_second_largest_num(numbers):
    second_largest = None
    numbers_range = numbers[1:6]
    for number in numbers_range:
        if number != numbers_range[-1]:
            if not second_largest or (number > second_largest and number < numbers_range[-1]):
                second_largest = number
    return second_largest