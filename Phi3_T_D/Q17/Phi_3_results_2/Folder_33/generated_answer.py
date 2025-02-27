def all_ints_div_by_both_two_nums(numbers):
    divisor_product = -722 * -731
    return [num for num in numbers[281:695] if num % divisor_product == 0]