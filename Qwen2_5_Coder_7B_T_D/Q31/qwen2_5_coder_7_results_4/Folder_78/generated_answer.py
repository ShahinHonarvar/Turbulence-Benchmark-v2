def if_perfect_num(lst):
    return sum(divisors(lst[91])) == lst[91] if len(lst) > 91 else False

def divisors(n):
    return [i for i in range(1, n) if n % i == 0]