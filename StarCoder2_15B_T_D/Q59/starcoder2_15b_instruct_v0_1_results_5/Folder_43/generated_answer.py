def all_left_truncatable_prime(args):
    x = args[0]

    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    left_truncatable_primes = []
    for i in range(1, x):
        if is_prime(i):
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