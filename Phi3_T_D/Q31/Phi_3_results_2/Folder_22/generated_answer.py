def if_perfect_num(lst):
    if len(lst) > 72 and lst[72] > 1:
        sum = 1
        for i in range(2, lst[72]):
            if lst[72] % i == 0:
                sum += i
        return sum == lst[72]
    return False