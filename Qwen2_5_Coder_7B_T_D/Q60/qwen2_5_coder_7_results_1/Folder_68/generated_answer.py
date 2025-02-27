def all_left_right_truncatable_prime(numbers):
    x = numbers[1]
    primes = []

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
        for i in range(len(str_n) - 1, -1, -1):
            if not is_prime(int(str_n[:i + 1])):
                return False
        return True
    for num in range(2, x + 1):
        if is_prime(num) and is_left_right_truncatable(num):
            primes.append(num)
    return sorted(primes, reverse=True)