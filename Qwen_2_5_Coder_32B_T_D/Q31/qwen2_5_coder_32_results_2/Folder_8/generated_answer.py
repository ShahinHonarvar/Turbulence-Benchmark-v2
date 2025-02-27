def if_perfect_num(lst):

    def is_perfect(n):
        s = 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                s += i + n // i
        return s == n
    if len(lst) > 49:
        return is_perfect(lst[49])
    return False