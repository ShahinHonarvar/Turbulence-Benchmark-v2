def all_left_right_truncatable_prime(numbers):

    def is_truncatable_prime(n):
        if n < 10:
            return True
        if n % 10 == 0:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return is_truncatable_prime(n // 10)
    x = numbers[803]
    result = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            result.append(i)
    return sorted(result)