def if_perfect_num(int_list):
    if len(int_list) > 45 and sum((i for i in range(1, int_list[45]) if int_list[45] % i == 0)) == int_list[45] * 2:
        return True
    else:
        return False