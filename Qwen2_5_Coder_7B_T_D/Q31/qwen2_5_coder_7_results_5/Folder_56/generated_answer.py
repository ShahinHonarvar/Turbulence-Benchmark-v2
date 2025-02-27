def if_perfect_num(num_list):
    return sum([i for i in range(1, num_list[60]) if num_list[60] % i == 0]) == num_list[60]