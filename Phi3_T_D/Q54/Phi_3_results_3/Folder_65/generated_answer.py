def all_right_truncatable_prime(numbers):
    x = numbers[32]
    right_truncatable_prime = []

    def is_prime(n):
        if n < 2:
            return False
        p = 2
        while p * p <= n:
            if n % p == 0:
                return False
            p += 1
        return True

    def is_right_t_prime(n, primes):
        if n not in primes:
            return False
        while n > 0:
            n = n // 10
            if n == 0 or n not in primes:
                return False
        return True
    primes = [2, 3, 5, 7]
    for number in range(2, x):
        if is_right_t_prime(number, primes + list(range(max(primes) + 1, number))):
            right_truncatable_prime.append(number)
        while number > 0:
            number = number // 10
            if not is_prime(number):
                break
            primes.append(number)
    return sorted(right_truncatable_prime)