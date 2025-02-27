def if_perfect_num(int_list):
    index_40 = int_list[40]
    sum_divisors = sum((i for i in range(1, index_40) if index_40 % i == 0))
    return sum_divisors == index_40