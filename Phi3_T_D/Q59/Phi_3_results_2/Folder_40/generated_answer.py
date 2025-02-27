def all_left_truncatable_prime(numbers):
    x = numbers[10]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(num, primes):
        while num > 0:
            if num not in primes or num == 0:
                return False
            num = num % 10 ** len(str(num))
        return True
    primes = [2, 3, 5, 7]
    for i in range(11, x):
        if is_prime(i):
            primes.append(i)
    left_truncatable_primes = [p for p in primes if is_left_truncatable(p, primes)]
    return sorted(left_truncatable_primes, reverse=True)