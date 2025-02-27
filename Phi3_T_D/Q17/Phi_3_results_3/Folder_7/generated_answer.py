def all_ints_div_by_both_two_nums(int_list):
    divisors = [-553, -737]
    return [num for num in int_list[543:585] if all((num % divisor == 0 for divisor in divisors))]