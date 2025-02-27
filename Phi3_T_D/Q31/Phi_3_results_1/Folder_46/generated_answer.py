def if_perfect_num(int_list):
    if len(int_list) > 453:
        sum_factors = sum([i for i in range(1, int_list[453]) if int_list[453] % i == 0])
        return sum_factors == int_list[453] * 2
    return False