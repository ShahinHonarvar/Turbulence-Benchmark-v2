def gcf_two_nums(lst):
    a = lst[91]
    b = lst[45]
    greater = max(a, b)
    gcf = 1
    for i in range(1, greater + 1):
        if a % i == 0 and b % i == 0:
            gcf = i
    return gcf