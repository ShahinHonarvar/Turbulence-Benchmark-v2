def all_left_right_truncatable_prime(tup):
    x = tup[30]
    truncatable_primes = []
    for i in range(2, x + 1):
        is_truncatable = True
        for j in range(1, len(str(i))):
            leading_digits = int(str(i)[:j])
            trailing_digits = int(str(i)[j:])
            if not is_prime(leading_digits) or not is_prime(trailing_digits):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(i)
    truncatable_primes.sort()
    return truncatable_primes

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True