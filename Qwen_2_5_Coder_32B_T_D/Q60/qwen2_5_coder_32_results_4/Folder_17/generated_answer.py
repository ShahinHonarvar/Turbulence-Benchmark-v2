def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[36]
    lr_trunc_primes = []
    for num in range(10, x + 1):
        s = str(num)
        if '0' in s:
            continue
        valid = True
        for i in range(1, len(s)):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:-i])):
                valid = False
                break
        if valid and is_prime(num):
            lr_trunc_primes.append(num)
    return sorted(lr_trunc_primes, reverse=True)