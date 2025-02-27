def all_right_truncatable_prime(numbers):
    x = numbers[466]
    primes = [2, 3, 5, 7]
    result = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    for num in range(11, x):
        if is_prime(num) and is_right_truncatable(num):
            result.append(num)
    return sorted(result, reverse=True)