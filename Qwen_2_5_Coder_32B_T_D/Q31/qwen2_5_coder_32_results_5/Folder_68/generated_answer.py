def if_perfect_num(lst):

    def is_perfect(n):
        s = 0
        for i in range(1, n):
            if n % i == 0:
                s += i
        return s == n
    return is_perfect(lst[3]) if len(lst) > 3 else False