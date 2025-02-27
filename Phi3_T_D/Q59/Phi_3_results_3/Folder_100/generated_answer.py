def all_left_truncatable_prime(numbers):
    if len(numbers) != 27 or not all((isinstance(n, int) and n > 0 for n in numbers)):
        raise ValueError('First argument must be a tuple of 27 positive integers.')
    primes = [2, 3, 5, 7]

    def is_prime(n):
        if n <= 1 or n in primes:
            return n in primes
        sqrt_n = int(n ** 0.5)
        for prime in primes:
            if prime > sqrt_n:
                break
            if n % prime == 0:
                return False
        primes.append(n)
        return True

    def left_truncatable_primes(n):
        if not is_prime(n):
            return []
        result = [n] if n % 10 != 0 else []
        return result + left_truncatable_primes(n / 10)
    x = numbers[26]
    trunc_primes = set()
    for num in range(2, int(x)):
        trunc_primes.update(left_truncatable_primes(num))
    return sorted(list(trunc_primes))