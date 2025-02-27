def all_right_truncatable_prime(numbers):
    x = numbers[81]
    prime_set = {2, 3, 5, 7}
    right_truncatable_primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        while n > 0:
            if n not in prime_set:
                return False
            n //= 10
        return True
    for num in range(2, x):
        if num in prime_set:
            right_truncatable_primes.append(num)
        elif is_prime(num):
            if is_right_truncatable(num):
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)