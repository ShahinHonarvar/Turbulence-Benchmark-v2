def gcf_three_nums(lst):

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    a, b, c = (lst[0], lst[4], lst[8])
    return gcf(gcf(a, b), c)