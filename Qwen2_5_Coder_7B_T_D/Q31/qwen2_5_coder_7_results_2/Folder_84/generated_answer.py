def if_perfect_num(lst):
    return sum((i for i in range(1, lst[685]) if lst[685] % i == 0)) == lst[685]