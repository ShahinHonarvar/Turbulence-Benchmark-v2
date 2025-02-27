def all_left_right_truncatable_prime(numbers):
    x = numbers[98]
    primes = [2, 3, 5, 7]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        str_n = str(n)
        if not is_prime(n):
            return False
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:i])):
                return False
        return True
    result = []
    for num in range(2, x + 1):
        if is_truncatable(num):
            result.append(num)
    return result