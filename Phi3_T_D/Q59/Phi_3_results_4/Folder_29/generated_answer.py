def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = [str(p) for p in range(2, int(numbers[-1])) if is_prime(p)]
    left_truncatables = []
    for prime in primes:
        for i in range(1, len(prime)):
            if not is_prime(int(prime[i:])):
                break
        else:
            left_truncatables.append(int(prime))
    return sorted(left_truncatables, reverse=True)