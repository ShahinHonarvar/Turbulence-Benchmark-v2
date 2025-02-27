def all_left_truncatable_prime(numbers):
    x = numbers[30]
    primes = [2, 3, 5, 7]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        while n:
            if not is_prime(n):
                return False
            n //= 10
        return True
    left_truncatable_primes = []
    for num in range(10, x):
        if is_prime(num) and '0' not in str(num) and is_left_truncatable(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)