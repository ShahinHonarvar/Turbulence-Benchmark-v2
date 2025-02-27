def all_ints_div_by_both_two_nums(lst):
    divisors = [-27, -96]
    divisible_nums = []
    for num in lst[36:86]:
        if all((num % divisor == 0 for divisor in divisors)):
            divisible_nums.append(num)
    return divisible_nums