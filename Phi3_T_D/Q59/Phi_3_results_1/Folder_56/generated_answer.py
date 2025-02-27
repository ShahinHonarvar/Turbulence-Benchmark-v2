def all_left_truncatable_prime(numbers):
    if not isinstance(numbers, tuple) or len(numbers) != 30:
        raise ValueError('Input must be a tuple of 30 positive integers.')

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n))):
            if not is_prime(int(str(n)[i:])):
                return False
        return True
    x = numbers[29]
    return sorted([p for p in range(2, x) if is_left_truncatable_prime(p)])