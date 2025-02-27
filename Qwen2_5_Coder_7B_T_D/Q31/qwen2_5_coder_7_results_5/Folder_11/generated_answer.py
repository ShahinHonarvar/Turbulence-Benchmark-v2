def if_perfect_num(num_list):
    if len(num_list) > 77:
        number = num_list[77]
        divisors_sum = sum((i for i in range(1, number) if number % i == 0))
        return divisors_sum == number
    else:
        return False