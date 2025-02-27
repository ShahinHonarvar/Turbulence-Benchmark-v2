def all_right_truncatable_prime(numbers):
    x = numbers[70]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if n < 10:
            return False
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    primes = [2, 3, 5, 7]
    truncables = []
    for num in range(7, x):
        if is_truncatable(num):
            truncables.append(num)
    return sorted(truncables, reverse=True)