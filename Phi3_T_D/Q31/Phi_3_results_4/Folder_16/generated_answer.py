def if_perfect_num(a_list):
    if len(a_list) > 162:
        sum_divisors = sum([i for i in range(1, a_list[162] // 2 + 1) if a_list[162] % i == 0])
        return sum_divisors == a_list[162]
    return False