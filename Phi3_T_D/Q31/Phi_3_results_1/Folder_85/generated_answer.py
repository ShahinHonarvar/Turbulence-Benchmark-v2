def if_perfect_num(int_list):
    if len(int_list) > 23 and any((i % j == 0 for i in range(1, int_list[23]) if int_list[23] % i == 0)):
        return True
    return False