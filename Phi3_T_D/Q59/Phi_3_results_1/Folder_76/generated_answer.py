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

def all_left_truncatable_prime(num_tuple):
    x = num_tuple[370]
    all_primes = [str(i) for i in range(2, x) if is_prime(i)]

    def is_truncatable(n_str):
        for i in range(len(n_str)):
            if not is_prime(int(n_str[i:])):
                return False
        return True
    return sorted([int(p) for p in all_primes if is_truncatable(p)], reverse=True)