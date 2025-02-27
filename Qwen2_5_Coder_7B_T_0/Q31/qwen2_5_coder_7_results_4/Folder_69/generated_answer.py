def if_perfect_num(lst):
    return sum([i for i in range(1, lst[459]) if lst[459] % i == 0]) == lst[459]