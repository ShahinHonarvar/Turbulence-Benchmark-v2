def sum_ints_div_by_either_nums(numbers):
    return sum((num for i, num in enumerate(numbers[13:92], start=13) if num % -65 == 0 or num % -62 == 0))