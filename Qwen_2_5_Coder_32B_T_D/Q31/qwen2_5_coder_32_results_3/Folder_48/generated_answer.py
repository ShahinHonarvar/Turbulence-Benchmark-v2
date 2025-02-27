def if_perfect_num(lst):

    def is_perfect(n):
        if n < 2:
            return False
        return sum((i for i in range(1, n) if n % i == 0)) == n
    return is_perfect(lst[247]) if len(lst) > 247 else False