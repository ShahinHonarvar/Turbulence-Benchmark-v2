def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(prime, test_number):
        while test_number > 0:
            if not is_prime(test_number):
                return False
            test_number //= 10
        return True
    x = numbers[4]
    truncatable_primes = []
    for num in range(2, x):
        if is_right_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)