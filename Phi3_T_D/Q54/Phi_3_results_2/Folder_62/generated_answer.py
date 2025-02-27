def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_primes_less_than(num):
    primes = [str(p) for p in range(2, num) if is_prime(p)]
    return sorted([int(p) for p in primes if all((is_prime(int(p[:i])) for i in range(len(p), 0, -1)))])

def all_right_truncatable_prime(numbers):
    x = numbers[70]
    return all_right_truncatable_primes_less_than(x)