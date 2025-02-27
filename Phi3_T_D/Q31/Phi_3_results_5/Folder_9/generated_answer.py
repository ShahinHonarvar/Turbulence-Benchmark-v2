def if_perfect_num(int_list):
    perfect = sum((i for i in range(1, int_list[24]) if int_list[24] % i == 0)) == int_list[24] * 2
    return perfect