def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[97]

    def truncatable_prime(n):
        if '0' in str(n) or not is_prime(n):
            return False
        s = str(n)
        while len(s) > 1:
            s = s[1:-1]
            if not is_prime(int(s)):
                return False
        return True
    return sorted([i for i in range(2, x + 1) if truncatable_prime(i)])