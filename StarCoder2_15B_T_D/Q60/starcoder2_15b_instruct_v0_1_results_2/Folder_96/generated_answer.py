def all_left_right_truncatable_prime(x):
    x = x[29]

    def is_truncatable_prime(num):
        if num < 10:
            return False
        if num in (11, 13, 17, 19, 23, 29):
            return True
        digits = list(str(num))
        for i in range(len(digits)):
            if not is_truncatable_prime(int(''.join(digits[i:]))):
                return False
            if not is_truncatable_prime(int(''.join(digits[:i + 1]))):
                return False
        return False
    primes = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            primes.append(i)
    return sorted(primes)