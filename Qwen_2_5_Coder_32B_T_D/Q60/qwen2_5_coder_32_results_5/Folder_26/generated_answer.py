def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[81]
    truncatable_primes = []
    for num in range(11, x + 1):
        s = str(num)
        if '0' in s:
            continue
        is_truncatable = True
        for i in range(1, len(s) - 1):
            if not is_prime(int(s[i:-1])) or not is_prime(int(s[i + 1:])):
                is_truncatable = False
                break
        if is_truncatable and is_prime(int(s[:-1])) and is_prime(int(s[1:])):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)