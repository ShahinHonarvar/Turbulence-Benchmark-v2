def if_perfect_num(lst):

    def is_perfect(n):
        s = sum((i for i in range(1, n) if n % i == 0))
        return s == n
    if len(lst) > 95:
        return is_perfect(lst[95])
    return False