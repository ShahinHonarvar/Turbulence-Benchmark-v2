def if_perfect_num(lst):

    def is_perfect(n):
        s = 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                s += i
                if i != n // i:
                    s += n // i
        return s == n if n > 1 else False
    return is_perfect(lst[99]) if len(lst) > 99 else False