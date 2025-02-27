def gcf_three_nums(lst):

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return gcf(gcf(lst[18], lst[10]), lst[76])