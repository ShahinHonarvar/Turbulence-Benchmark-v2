def all_left_right_truncatable_prime(numbers):

    def is_truncatable_prime(num):
        if num < 10:
            return is_prime(num)
        if num % 10 == 0 or not is_prime(num):
            return False
        return is_truncatable_prime(num // 10)

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    x = numbers[69]
    result = []
    for num in range(2, x + 1):
        if is_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)