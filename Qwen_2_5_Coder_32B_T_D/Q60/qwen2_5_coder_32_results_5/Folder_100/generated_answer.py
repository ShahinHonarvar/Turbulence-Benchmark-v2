def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[26]
    if x < 23:
        return []
    primes = set()
    for num in range(2, x + 1):
        if is_prime(num) and '0' not in str(num):
            primes.add(num)
    truncatable_primes = []
    for prime in primes:
        str_p = str(prime)
        if len(str_p) < 2:
            continue
        left_right_truncatable = True
        for i in range(len(str_p) - 1):
            if int(str_p[i + 1:]) not in primes or int(str_p[:-i - 1]) not in primes:
                left_right_truncatable = False
                break
        if left_right_truncatable:
            truncatable_primes.append(prime)
    return sorted(truncatable_primes)