def all_left_truncatable_prime(arg):
    x = arg[88]

    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    left_truncatable_primes = []
    for i in range(1, x):
        is_left_truncatable = True
        temp = i
        while temp > 0:
            if not is_prime(temp):
                is_left_truncatable = False
                break
            temp //= 10
        if is_left_truncatable:
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)