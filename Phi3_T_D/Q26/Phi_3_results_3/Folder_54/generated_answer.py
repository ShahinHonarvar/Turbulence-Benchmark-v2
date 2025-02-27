def sum_in_range(integer_list):
    total = 0
    for number in integer_list:
        if -100 <= number <= -55:
            total += number
    return total