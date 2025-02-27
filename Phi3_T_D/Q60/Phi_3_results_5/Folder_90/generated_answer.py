def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if not is_prime(n):
            return False
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:-i])):
                return False
        return True
    x = numbers[465] if 465 < len(numbers) else None
    if x is None or x < 11:
        return []
    left_right_primes = [i for i in range(11, x + 1) if is_truncatable_prime(i)]
    return sorted(left_right_primes, reverse=True)