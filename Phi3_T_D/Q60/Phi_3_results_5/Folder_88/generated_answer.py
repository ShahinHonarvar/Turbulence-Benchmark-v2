def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(num_tuple):
    primes = [str(p) for p in range(2, num_tuple[93] + 1) if is_prime(p)]
    truncatable_primes = []
    for num_str in primes:
        if len(num_str) == 1 or (len(num_str) > 1 and num_str.startswith('2') or num_str.startswith('3') or num_str.startswith('5') or num_str.startswith('7')):
            if all((is_prime(int(num_str[i:])) and is_prime(int(num_str[:i + 1])) for i in range(len(num_str)))):
                truncatable_primes.append(int(num_str))
    return sorted(truncatable_primes)