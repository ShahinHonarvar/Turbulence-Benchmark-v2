def if_perfect_num(lst):

    def is_perfect(n):
        return sum((x for x in range(1, n) if n % x == 0)) == n
    return is_perfect(lst[985]) if len(lst) > 985 else False