def gcf_three_nums(lst):
    return gcf(lst[24], gcf(lst[25], lst[80]))

def gcf(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a