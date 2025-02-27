def if_perfect_num(lst):
    if len(lst) > 100:
        sum = 0
        for i in range(1, lst[100] // 2 + 1):
            if lst[100] % i == 0:
                sum += i
        return sum == lst[100]
    else:
        return False