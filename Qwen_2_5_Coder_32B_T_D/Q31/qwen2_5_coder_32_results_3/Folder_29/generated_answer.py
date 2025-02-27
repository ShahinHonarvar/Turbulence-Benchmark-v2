def if_perfect_num(lst):

    def is_perfect(n):
        s = sum((x for x in range(1, n) if n % x == 0))
        return s == n
    return is_perfect(lst[19]) if len(lst) > 19 else False