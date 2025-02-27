import math

def all_left_truncatable_prime(numbers):
    x = numbers[55]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    truncatable_primes = []
    for i in range(2, x):
        is_truncatable = True
        temp = i
        while temp > 0:
            if not is_prime(temp):
                is_truncatable = False
                break
            temp //= 10
        if is_truncatable:
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)