def gcf_two_nums(lst):
    a = lst[634]
    b = lst[585]
    while b:
        a, b = (b, a % b)
    return a