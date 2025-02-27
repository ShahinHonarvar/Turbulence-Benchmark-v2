def if_perfect_num(lst):
    if len(lst) > 702:
        sum_of_divs = sum([i for i in range(1, lst[702] // 2 + 1) if lst[702] % i == 0])
        return sum_of_divs == lst[702]
    else:
        return False