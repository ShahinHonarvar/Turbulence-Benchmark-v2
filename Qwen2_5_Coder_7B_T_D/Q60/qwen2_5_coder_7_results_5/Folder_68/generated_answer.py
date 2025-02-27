def all_left_right_truncatable_prime(numbers):

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
        num = n
        while num >= 10:
            num //= 10
            if not is_prime(num):
                return False
        num = n
        while num >= 10:
            num %= 10 ** len(str(num)) // 10
            if not is_prime(num):
                return False
        return True
    x = numbers[1]
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_prime(num) and is_left_right_truncatable(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)