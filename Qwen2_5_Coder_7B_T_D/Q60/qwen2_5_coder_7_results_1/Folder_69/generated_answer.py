def all_left_right_truncatable_prime(numbers):
    x = numbers[760]
    left_right_truncatable_primes = []

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_left_right_truncatable(n):
        if '0' in str(n):
            return False
        str_n = str(n)
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
        for i in range(len(str_n) - 1, 0, -1):
            if not is_prime(int(str_n[:i])):
                return False
        return True
    for num in range(2, x + 1):
        if is_prime(num) and is_left_right_truncatable(num):
            left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes, reverse=True)