import math

def all_left_right_truncatable_prime(numbers):
    x = numbers[78]
    primes = []

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True

    def is_right_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    for num in range(2, x + 1):
        if str(num).find('0') == -1 and is_prime(num) and is_left_truncatable_prime(num) and is_right_truncatable_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)