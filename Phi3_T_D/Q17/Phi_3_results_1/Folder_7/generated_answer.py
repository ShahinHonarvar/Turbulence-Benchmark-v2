def all_ints_div_by_both_two_nums(numbers):
    start_index = 543
    end_index = 584
    divisor1 = -553
    divisor2 = -737
    divisible_numbers = [number for number in numbers[start_index:end_index + 1] if number % divisor1 == 0 and number % divisor2 == 0]
    return divisible_numbers