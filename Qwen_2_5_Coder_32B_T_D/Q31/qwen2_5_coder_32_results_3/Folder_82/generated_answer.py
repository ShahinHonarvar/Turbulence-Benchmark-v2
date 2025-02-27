def if_perfect_num(lst):

    def is_perfect(n):
        return n == sum((x for x in range(1, n) if n % x == 0))
    return is_perfect(lst[83]) if len(lst) > 83 else False