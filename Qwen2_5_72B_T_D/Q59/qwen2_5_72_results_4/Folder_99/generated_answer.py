def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[758]

    def is_left_truncatable_prime(n):
        for i in range(1, len(str(n))):
            if not is_prime(int(str(n)[i:])):
                return False
        return True
    result = []
    for i in range(2, x):
        if is_prime(i) and '0' not in str(i) and is_left_truncatable_prime(i):
            result.append(i)
    return result