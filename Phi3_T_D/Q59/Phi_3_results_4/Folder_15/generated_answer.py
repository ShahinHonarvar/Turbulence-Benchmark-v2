def all_left_truncatable_prime(numbers):
    x = numbers[6]
    primes = [2, 3, 5, 7]
    left_truncatable_primes = []

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n, primes):
        while n > 0:
            if not is_prime(n):
                return False
            n = n % 10 ** (len(str(n)) - 1)
        return True
    for number in range(23, x):
        if is_left_truncatable(number, primes):
            left_truncatable_primes.append(number)
    return left_truncatable_primes[::-1]