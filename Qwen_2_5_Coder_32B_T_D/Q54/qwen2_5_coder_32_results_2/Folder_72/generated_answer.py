def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        while n:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = numbers[31]
    result = [n for n in range(2, x) if is_right_truncatable_prime(n)]
    return sorted(result, reverse=True)