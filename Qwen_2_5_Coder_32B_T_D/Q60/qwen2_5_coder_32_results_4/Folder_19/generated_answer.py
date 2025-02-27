def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[67]
    lr_truncatable_primes = []
    for num in range(23, x + 1):
        s = str(num)
        if '0' not in s:
            all_truncations_prime = True
            for i in range(1, len(s) - 1):
                if not is_prime(int(s[i:])) or not is_prime(int(s[:-i])):
                    all_truncations_prime = False
                    break
            if all_truncations_prime and is_prime(int(s[1:])) and is_prime(int(s[:-1])):
                lr_truncatable_primes.append(num)
    return sorted(lr_truncatable_primes, reverse=True)