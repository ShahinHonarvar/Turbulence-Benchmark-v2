def all_left_right_truncatable_prime(numbers):
    x = numbers[33]

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
        n_str = str(n)
        for i in range(len(n_str)):
            if '0' in n_str[i:]:
                break
            left_trunc = int(n_str[i:])
            right_trunc = int(n_str[:len(n_str) - i])
            if not is_prime(left_trunc) or not is_prime(right_trunc):
                break
        return i == len(n_str) - 1
    truncatable_primes = [n for n in range(2, x + 1) if is_prime(n) and is_left_right_truncatable(n)]
    return sorted(truncatable_primes)