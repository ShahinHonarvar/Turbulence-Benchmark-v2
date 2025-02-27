def if_perfect_num(num_list):
    perfect_sum = sum([i for i in range(1, num_list[746] // 2 + 1) if num_list[746] % i == 0])
    return perfect_sum == num_list[746]