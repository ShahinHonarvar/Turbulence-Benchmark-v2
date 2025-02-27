def if_perfect_num(num_list):
    divisor_sum = sum([i for i in range(1, num_list[66] // 2 + 1) if num_list[66] % i == 0])
    return divisor_sum == num_list[66]