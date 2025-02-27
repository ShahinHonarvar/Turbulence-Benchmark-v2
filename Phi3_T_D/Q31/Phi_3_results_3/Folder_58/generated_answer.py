def if_perfect_num(lst):
    perfect = lambda n: sum((i for i in range(1, n) if n % i == 0)) == n
    if 714 < len(lst) and perfect(lst[714]):
        return True
    return False