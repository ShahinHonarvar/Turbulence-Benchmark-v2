def all_right_truncatable_prime(numbers):
    x = numbers[88]
    truncatable_primes = [2, 3, 5, 7]
    is_prime_cache = [None] * (x + 1)

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if is_prime_cache[n]:
            return is_prime_cache[n]
        if n % 2 == 0 or n % 3 == 0:
            is_prime_cache[n] = False
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                is_prime_cache[n] = False
                return False
            i += 6
        is_prime_cache[n] = True
        return True

    def is_truncatable_prime(number):
        while number > 0:
            if not is_prime(number):
                return False
            number = int(str(number)[:-1])
        return True
    return sorted([p for p in range(11, x, 2) if is_prime(p) and is_truncatable_prime(p)], reverse=True)