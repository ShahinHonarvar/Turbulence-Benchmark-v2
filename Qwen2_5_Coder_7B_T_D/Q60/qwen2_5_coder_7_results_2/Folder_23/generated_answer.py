def all_left_right_truncatable_prime(numbers):
    x = numbers[77]
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

    def is_truncatable_prime(n):
        s = str(n)
        while len(s) > 1:
            if not is_prime(int(s)):
                return False
            s = s[1:]
            s = s[:-1]
        return True
    for num in range(2, x + 1):
        if '0' not in str(num) and is_prime(num) and is_truncatable_prime(num):
            left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes, reverse=True)