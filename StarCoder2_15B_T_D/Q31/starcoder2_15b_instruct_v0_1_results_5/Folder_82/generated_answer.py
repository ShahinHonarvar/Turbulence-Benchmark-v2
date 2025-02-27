def if_perfect_num(num_list):
    if num_list[83] == sum((i for i in range(1, num_list[83]) if num_list[83] % i == 0)):
        return True
    return False