from sympy import isprime

def is_right_truncatable_prime(n):
    str_n = str(n)
    while len(str_n) > 1:
        if not isprime(int(str_n)):
            return False
        str_n = str_n[:-1]
    return True

def all_right_truncatable_prime(nums_tuple):
    x = nums_tuple[54]
    return sorted([p for p in range(x - 1, 1, -1) if p % 10 > 1 and is_right_truncatable_prime(p)], reverse=True)