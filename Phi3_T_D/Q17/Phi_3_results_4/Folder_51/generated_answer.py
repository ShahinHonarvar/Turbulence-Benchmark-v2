def all_ints_div_by_both_two_nums(int_list):
    output = []
    divisors = [-1, -10]
    for number in int_list[6:10]:
        if all((number % divisor == 0 for divisor in divisors)):
            output.append(number)
    return output