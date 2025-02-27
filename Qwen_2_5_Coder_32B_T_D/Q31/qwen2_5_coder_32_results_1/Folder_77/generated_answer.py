def if_perfect_num(lst):

    def is_perfect(n):
        s = sum((i for i in range(1, n) if n % i == 0))
        return s == n
    return is_perfect(lst[985]) if len(lst) > 985 else False