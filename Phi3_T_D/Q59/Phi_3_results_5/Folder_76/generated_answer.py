def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n, sieve):
        while n > 0:
            if not sieve[n]:
                return False
            n = int(str(n)[1:]) if n > 0 else 0
        return True
    sieve = [True] * (numbers[370] + 1)
    for i in range(2, int(numbers[370] ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, numbers[370] + 1, i):
                sieve[j] = False
    left_truncatable_primes = [p for p in range(2, numbers[370]) if is_prime(p) and is_left_truncatable_prime(p, sieve)]
    return left_truncatable_primes[::-1]