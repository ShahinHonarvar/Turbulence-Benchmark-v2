def all_ints_div_by_both_two_nums(int_list):
    start, end = (20, 93)
    divisors = [-92, -50]
    divisible_integers = [num for num in int_list[start:end + 1] if all((num % div == 0 for div in divisors))]
    return divisible_integers