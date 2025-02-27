def all_left_right_truncatable_prime(numbers):
    x = numbers[37]

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
        for i in range(len(str_n) - 1, 0, -1):
            if not is_prime(int(str_n[:i])):
                return False
        return True
    left_right_truncatable_primes = []
    for num in range(2, x + 1):
        if str(num).count('0') == 0 and is_left_right_truncatable(num):
            left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes, reverse=True)