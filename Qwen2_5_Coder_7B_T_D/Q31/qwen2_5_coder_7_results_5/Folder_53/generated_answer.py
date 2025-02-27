def if_perfect_num(num_list):
    if 73 < len(num_list):
        num = num_list[73]
        sum_divisors = sum([i for i in range(1, num) if num % i == 0])
        return sum_divisors == num
    return False