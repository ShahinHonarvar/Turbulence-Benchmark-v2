def gcf_two_nums(lst):
    a, b = (lst[180], lst[312])
    while b:
        a, b = (b, a % b)
    return a