def if_perfect_num(num_list):
    number = num_list[27]
    sum_of_factors = sum((factor for factor in range(1, number) if number % factor == 0))
    return sum_of_factors == number