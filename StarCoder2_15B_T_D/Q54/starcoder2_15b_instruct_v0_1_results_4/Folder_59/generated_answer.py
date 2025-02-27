def all_right_truncatable_prime(numbers):
    x = numbers[84]

    def is_right_truncatable_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    result = []
    for i in range(x):
        n = i
        while n > 0:
            if not is_right_truncatable_prime(n):
                break
            n //= 10
        else:
            result.append(i)
    return sorted(result, reverse=True)