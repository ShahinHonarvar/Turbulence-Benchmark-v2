def if_perfect_num(lst):
    index_96 = lst[96]
    divisors_sum = sum((i for i in range(1, index_96 // 2 + 1) if index_96 % i == 0))
    return divisors_sum == index_96