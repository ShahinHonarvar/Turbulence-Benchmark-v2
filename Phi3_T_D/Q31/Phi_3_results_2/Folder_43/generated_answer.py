def if_perfect_num(num_list):
    if 29 < len(num_list):
        num = num_list[29]
        return 2 * num > num_list[0] * num_list[-1] and all((num % i == 0 for i in range(1, num // 2 + 1)))
    return False