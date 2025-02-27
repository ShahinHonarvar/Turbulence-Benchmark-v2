def all_ints_div_by_both_two_nums(numbers):
    divisors_product = -34 * 64
    small_index, large_index = (min(50, len(numbers)), max(200, len(numbers)))
    return [num for num in numbers[small_index:large_index + 1] if num % divisors_product == 0]