def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(p):
        if '0' in str(p):
            return False
        s = str(p)
        while s:
            if not is_prime(int(s)):
                return False
            s = s[1:-1]
        return True
    x = numbers[992]
    primes = []
    for num in range(2, x + 1):
        if is_prime(num) and is_truncatable(num):
            primes.append(num)
    return sorted(primes)