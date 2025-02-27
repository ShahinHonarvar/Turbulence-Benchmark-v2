def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    str_n = str(n)
    for i in range(len(str_n)):
        if not is_prime(int(str_n[i:])):
            return False
        if i > 0 and (not is_prime(int(str_n[:i + 1]))):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[22]
    truncatable_primes = [i for i in range(x, 1, -1) if is_truncatable_prime(i)]
    return truncatable_primes