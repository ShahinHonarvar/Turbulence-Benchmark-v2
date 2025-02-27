def all_left_truncatable_prime(args):
    x = args[29]

    def is_truncatable_prime(n):
        if n < 2 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    truncatable_primes = []
    for i in range(2, x):
        is_prime = True
        temp = i
        while temp > 0:
            if not is_truncatable_prime(temp):
                is_prime = False
                break
            temp //= 10
        if is_prime:
            truncatable_primes.append(i)
    return sorted(truncatable_primes)