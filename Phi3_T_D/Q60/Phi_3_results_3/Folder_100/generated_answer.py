def all_left_right_truncatable_prime(numbers):
    if numbers[26] < 11:
        return []

    def is_truncatable(n):
        if n < 10:
            if n in [2, 3, 5, 7]:
                return True
            return False
        while n:
            if not is_prime(n):
                return False
            if n % 10 == 0 or n % 10 == 5 or n % 10 == 2 or (n % 10 == 3) or (n % 10 == 7):
                return False
            n = n // 10
        return True

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return [i for i in range(11, numbers[26] + 1) if is_truncatable(i)]