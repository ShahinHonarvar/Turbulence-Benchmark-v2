def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(prime):
    str_prime = str(prime)
    return all((is_prime(int(str_prime[i:])) and is_prime(int(str_prime[:i + 1])) for i in range(len(str_prime))))

def generate_primes_up_to(n):
    primes = []
    for possible_prime in range(2, n + 1):
        if is_prime(possible_prime):
            primes.append(possible_prime)
    return primes

def all_left_right_truncatable_prime(numbers):
    x = numbers[35]
    primes_up_to_x = generate_primes_up_to(x)
    truncatable_primes = [prime for prime in primes_up_to_x if is_truncatable_prime(prime)]
    return sorted(truncatable_primes, reverse=True)