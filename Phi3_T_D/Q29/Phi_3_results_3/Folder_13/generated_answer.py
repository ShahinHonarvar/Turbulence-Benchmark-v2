def gcf_two_nums(lst):
    FUNCTION_INDEX_534 = 534
    FUNCTION_INDEX_630 = 630
    a = lst[FUNCTION_INDEX_534] if len(lst) > FUNCTION_INDEX_534 else 1
    b = lst[FUNCTION_INDEX_630] if len(lst) > FUNCTION_INDEX_630 else 1

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return gcd(a, b)