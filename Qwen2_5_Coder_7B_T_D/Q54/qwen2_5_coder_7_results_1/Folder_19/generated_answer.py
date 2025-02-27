def all_right_truncatable_prime(numbers):
    x = numbers[67]
    primes = []

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        for i in range(1, len(str(n)) + 1):
            if not is_prime(int(str(n)[:i])):
                return False
        return True
    for num in range(2, x):
        if is_prime(num) and is_right_truncatable(num):
            primes.append(num)
    return sorted(primes, reverse=True)