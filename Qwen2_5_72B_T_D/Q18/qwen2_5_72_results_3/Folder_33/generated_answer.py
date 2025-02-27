def sum_ints_div_by_either_nums(numbers):
    return sum((num for i, num in enumerate(numbers[281:695]) if num % -722 == 0 or num % -731 == 0))