def gcf_three_nums(lst):
    return reduce(lambda x, y: gcd(x, y), [lst[4], lst[0], lst[8]])