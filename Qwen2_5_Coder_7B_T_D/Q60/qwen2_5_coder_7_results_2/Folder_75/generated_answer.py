def all_left_right_truncatable_prime(numbers):
    x = numbers[41]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        if '0' in str(n):
            return False
        str_n = str(n)
        while len(str_n) > 1:
            if not is_prime(int(str_n)):
                return False
            str_n = str_n[1:]
            str_n = str_n[:-1]
        return is_prime(int(str_n))
    left_right_truncatable_primes = []
    for num in range(2, x + 1):
        if is_left_right_truncatable(num):
            left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes)