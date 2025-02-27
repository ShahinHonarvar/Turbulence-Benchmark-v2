def gcf_three_nums(lst):

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    if len(lst) < 771:
        return None
    a, b, c = (lst[145], lst[183], lst[770])
    return gcf(gcf(a, b), c)