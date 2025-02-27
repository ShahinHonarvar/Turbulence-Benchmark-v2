def if_perfect_num(int_list):
    if len(int_list) > 60:
        div_sum = sum([i for i in range(1, int_list[60] // 2 + 1) if int_list[60] % i == 0])
        return div_sum == int_list[60]
    return False