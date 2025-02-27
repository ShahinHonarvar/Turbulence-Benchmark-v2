def gcf_three_nums(lst):

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    a, b, c = (lst[341], lst[238], lst[374])
    return gcf(gcf(a, b), c)