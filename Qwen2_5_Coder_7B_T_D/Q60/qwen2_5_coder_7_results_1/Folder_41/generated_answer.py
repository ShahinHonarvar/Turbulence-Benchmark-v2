def all_left_right_truncatable_prime(numbers):
    x = numbers[46]
    primes = [2, 3, 5, 7]
    left_right_truncatable = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
            if not is_prime(int(str_n[:i + 1])):
                return False
        return True
    for num in range(2, x + 1):
        if '0' not in str(num) and is_prime(num) and is_left_right_truncatable(num):
            left_right_truncatable.append(num)
    return sorted(left_right_truncatable, reverse=True)