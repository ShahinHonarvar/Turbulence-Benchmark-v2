def gcf_three_nums(lst):

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    a, b, c = (lst[56], lst[54], lst[13])
    return gcf(gcf(a, b), c)