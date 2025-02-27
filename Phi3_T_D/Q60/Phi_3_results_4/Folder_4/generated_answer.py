def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[96]
    truncatable_primes = []

    def is_truncatable_prime(num):
        if not num:
            return False
        str_num = str(num)
        for i in range(1, len(str_num) // 2 + 1):
            if not (is_prime(int(str_num[i:])) and is_prime(int(str_num[:-i or None]))):
                return False
        return True
    for prime in range(2, x + 1):
        if is_prime(prime) and is_truncatable_prime(prime):
            truncatable_primes.append(prime)
    return sorted(truncatable_primes, reverse=True)