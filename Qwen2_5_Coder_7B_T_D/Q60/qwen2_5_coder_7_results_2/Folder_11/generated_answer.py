def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[86]
    truncatable_primes = []
    for num in range(2, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        if not is_prime(num):
            continue
        if all((is_prime(int(str_num[:i])) and is_prime(int(str_num[-i:])) for i in range(1, len(str_num)))):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)