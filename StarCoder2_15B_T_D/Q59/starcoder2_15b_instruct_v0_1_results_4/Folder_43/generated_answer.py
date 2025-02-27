def all_left_truncatable_prime(numbers):
    x = numbers[89]

    def is_left_truncatable_prime(n):
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
        if is_left_truncatable_prime(i):
            result.append(i)
    result.sort(reverse=True)
    return result