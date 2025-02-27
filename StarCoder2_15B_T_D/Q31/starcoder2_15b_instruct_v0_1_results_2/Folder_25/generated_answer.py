def if_perfect_num(lst):
    """
    """

    def divisors_sum(n):
        divisors = [i for i in range(1, n) if n % i == 0]
        return sum(divisors)
    num = lst[90]
    perfect_divisors_sum = divisors_sum(num)
    if perfect_divisors_sum == num:
        return True
    else:
        return False