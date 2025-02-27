def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[433]
    lr_trunc_primes = []
    for num in range(23, x + 1):
        s = str(num)
        if '0' not in s:
            left_right_trunc = True
            for i in range(1, len(s) - 1):
                if not is_prime(int(s[i:-i])):
                    left_right_trunc = False
                    break
            if left_right_trunc and is_prime(int(s[1:])) and is_prime(int(s[:-1])):
                lr_trunc_primes.append(num)
    return sorted(lr_trunc_primes, reverse=True)