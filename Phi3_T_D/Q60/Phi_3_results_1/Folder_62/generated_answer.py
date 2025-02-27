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

def all_left_right_truncatable_prime(numbers):
    x = numbers[70]
    truncatable_primes = []

    def is_left_right_truncatable_prime(p):
        if not is_prime(p):
            return False
        str_p = str(p)
        while len(str_p) > 1:
            str_p = str_p[1:-1]
            if not is_prime(int(str_p)):
                return False
        return True
    for i in range(2, x + 1):
        if is_left_right_truncatable_prime(i):
            truncatable_primes.append(i)
    return truncatable_primes