def all_left_right_truncatable_prime(numbers):
    x = numbers[26]
    primes = [2, 3, 5, 7]
    truncatable_primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        s = str(n)
        for i in range(len(s)):
            if not is_prime(int(s[i:])):
                return False
            if not is_prime(int(s[:len(s) - i])):
                return False
        return True
    for num in range(10, x + 1):
        if is_prime(num) and '0' not in str(num) and is_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)