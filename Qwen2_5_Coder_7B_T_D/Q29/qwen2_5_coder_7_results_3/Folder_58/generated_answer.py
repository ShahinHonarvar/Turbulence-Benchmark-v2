def gcf_two_nums(lst):
    a, b = (lst[129], lst[582])
    while b:
        a, b = (b, a % b)
    return a