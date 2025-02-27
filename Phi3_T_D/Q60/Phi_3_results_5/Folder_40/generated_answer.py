def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_and_right_truncatable_prime(n, primes):
    str_n = str(n)
    for i in range(1, len(str_n)):
        if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:i])):
            return False
    return True

def all_left_right_truncatable_prime(input_tuple):
    upper_limit = input_tuple[10]
    primes = [i for i in range(2, upper_limit) if is_prime(i)]
    return sorted([p for p in primes if is_left_and_right_truncatable_prime(p, primes)], reverse=True)