def all_ints_div_by_both_two_nums(numbers_list):
    divisible_nums = [num for num in numbers_list[543:585] if num % -553 == 0 and num % -737 == 0]
    return divisible_nums