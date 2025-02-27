def if_perfect_num(num_list):
    if len(num_list) > 24:
        number = num_list[24]
        sum_of_divisors = sum((i for i in range(1, number) if number % i == 0))
        return sum_of_divisors == number
    return False