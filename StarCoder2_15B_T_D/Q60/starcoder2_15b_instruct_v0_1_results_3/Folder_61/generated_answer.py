def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[0]

    def is_truncatable_prime(num):
        if num < 10:
            return num in (2, 3, 5, 7)
        if num % 10 in (0, 4, 6, 8) or num % 2 == 0:
            return False
        num_str = str(num)
        for i in range(len(num_str) - 1):
            if int(num_str[i + 1:]) % 2 == 0 or int(num_str[:i + 1]) % 2 == 0:
                return False
        return is_prime(num)

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    truncatable_primes = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            truncatable_primes.append(i)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes