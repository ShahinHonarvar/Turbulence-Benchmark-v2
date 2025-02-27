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

def all_left_right_truncatable_prime(numbers):
    x = numbers[20]
    truncatable_primes = []

    def is_left_right_truncatable(n):
        digits = str(n)
        if '0' in digits:
            return False
        while digits:
            if not is_prime(int(digits)):
                return False
            digits = digits[1:-1]
        return True
    for num in range(2, x + 1):
        if is_left_right_truncatable(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)