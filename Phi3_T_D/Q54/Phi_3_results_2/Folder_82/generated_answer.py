def all_right_truncatable_prime(numbers):
    x = numbers[69] if len(numbers) > 69 else None
    if x is None or x < 11:
        return []

    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        p = 3
        while p * p <= n:
            if n % p == 0:
                return False
            p += 2
        return True

    def truncatable(n):
        if not is_prime(n):
            return False
        temp = n
        while temp > 0:
            if not is_prime(temp):
                return False
            temp = temp // 10
        return True
    return sorted([n for n in range(11, x) if truncatable(n)], reverse=True)