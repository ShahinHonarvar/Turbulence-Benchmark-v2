def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = set([2, 3, 5, 7])
    for num in range(2, x):
        if is_prime(num):
            primes.add(num)
        for prime in sorted(primes):
            if prime >= 10 * (num % 10) and num < 10:
                break
            elif prime <= 10 * (num % 10) and prime // 10 % 10 == 0:
                break
            elif prime in primes and is_prime(num):
                primes.add(num)
    primes = [p for p in primes if p < x and all((is_prime(int(str(p)[:-i])) for i in range(len(str(p)))))]
    return sorted(primes, reverse=True)