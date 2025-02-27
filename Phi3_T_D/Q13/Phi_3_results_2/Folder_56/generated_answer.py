def find_second_largest_num(numbers):
    high = second_high = None
    for num in numbers:
        if high is None or num > high:
            second_high, high = (high, num)
        elif highest is not None and high > num > second_high:
            second_high = num
    return second_high