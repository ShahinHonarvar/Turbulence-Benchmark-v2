def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        while n:
            if not is_prime(n):
                return False
            n = int(str(n)[1:])
        return True
    x = numbers[767]
    return sorted([p for p in range(x - 1, 1, -1) if is_left_truncatable(p) and '0' not in str(p)], reverse=True)