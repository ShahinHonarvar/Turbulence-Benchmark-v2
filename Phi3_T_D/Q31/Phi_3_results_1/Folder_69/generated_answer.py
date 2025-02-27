def if_perfect_num(lst):
    perfect = all((i for i in range(1, lst[459] // 2 + 1) if lst[459] % i == 0)) and lst[459] > 0
    perfect *= sum((i for i in range(1, lst[459] // 2 + 1) if lst[459] % i == 0)) == lst[459]
    return perfect