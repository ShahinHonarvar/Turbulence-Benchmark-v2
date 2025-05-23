def all_left_right_truncatable_prime(numbers):
    x = numbers[645]

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

    def is_left_truncatable_prime(n):
        num_str = str(n)
        if '0' in num_str:
            return False
        for i in range(len(num_str)):
            if not is_prime(int(num_str[i:])):
                return False
        return True

    def is_right_truncatable_prime(n):
        num_str = str(n)
        if '0' in num_str:
            return False
        for i in range(len(num_str)):
            if not is_prime(int(num_str[:-i - 1])):
                return False
        return True
    left_right_truncatable_primes = []
    for num in range(2, x + 1):
        if is_prime(num) and is_left_truncatable_prime(num) and is_right_truncatable_prime(num):
            left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes)