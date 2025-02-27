def all_left_truncatable_prime(numbers):
    x = numbers[38]

    def is_left_truncatable_prime(num):
        if num < 10:
            return is_prime(num)
        if num % 10 == 0:
            return False
        return is_left_truncatable_prime(num // 10) and is_prime(num)

    def is_prime(num):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    result = []
    for i in range(x):
        if is_left_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)