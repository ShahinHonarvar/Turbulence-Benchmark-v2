def if_perfect_num(lst):

    def is_perfect(n):
        s = sum([f for f in range(1, n) if n % f == 0])
        return s == n
    return is_perfect(lst[45]) if len(lst) > 45 else False