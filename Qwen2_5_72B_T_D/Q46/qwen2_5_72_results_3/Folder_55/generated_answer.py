def gcf_three_nums(lst):

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    a = lst[2]
    b = lst[6]
    c = lst[9]
    return gcf(gcf(a, b), c)