def if_perfect_num(lst):
    if 453 >= len(lst):
        return False
    num = lst[453]
    s = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            s += i
            if i != num // i:
                s += num // i
    return s == num