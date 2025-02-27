def all_ints_div_by_both_two_nums(numbers):
    divisor_product = -863 * -329
    return [num for num in numbers[138:425] if num % divisor_product == 0]