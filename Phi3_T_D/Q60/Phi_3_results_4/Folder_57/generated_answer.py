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

def all_left_right_truncatable_prime(num_tuple):
    x = num_tuple[54]
    truncatable_primes = []
    primes = [str(i) for i in range(2, x + 1) if is_prime(i)]
    for prime_str in primes:
        for i in range(len(prime_str)):
            if not is_prime(int(prime_str[i:])) or not is_prime(int(prime_str[:len(prime_str) - i])):
                break
        else:
            truncatable_primes.append(int(prime_str))
    return sorted(truncatable_primes, reverse=True)