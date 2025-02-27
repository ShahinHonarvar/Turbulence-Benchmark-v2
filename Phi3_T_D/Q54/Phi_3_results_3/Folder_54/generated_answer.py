def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[88]
    truncatable_primes = []

    def is_right_truncatable_prime(num):
        if not is_prime(num):
            return False
        temp = num
        while temp > 0:
            if not is_prime(temp):
                return False
            temp //= 10
        return True
    for num in range(x - 1, 10, -1):
        if is_right_truncatable_prime(num):
            truncatable_primes.append(num)
    return truncatable_primes if truncatable_primes else []