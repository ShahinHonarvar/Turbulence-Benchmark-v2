def if_perfect_num(num_list):
    if len(num_list) > 92:
        sum_divisors = sum((i for i in range(1, num_list[92] // 2 + 1) if num_list[92] % i == 0))
        return sum_divisors == num_list[92]
    return False