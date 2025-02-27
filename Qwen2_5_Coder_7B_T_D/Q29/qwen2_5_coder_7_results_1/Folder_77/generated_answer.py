def gcf_two_nums(lst):
    a = lst[841]
    b = lst[804]
    while b:
        a, b = (b, a % b)
    return a