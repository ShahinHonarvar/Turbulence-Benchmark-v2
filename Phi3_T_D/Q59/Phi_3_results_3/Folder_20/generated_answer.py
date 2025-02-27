def all_left_truncatable_prime(numbers):
    x = numbers[100]

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable_prime(prime):
        while prime > 0:
            if not is_prime(prime):
                return False
            prime = int(str(prime)[1:])
        return True
    primes_under_x = [p for p in range(2, x) if is_prime(p)]
    return sorted([p for p in primes_under_x if is_left_truncatable_prime(p)], reverse=True)