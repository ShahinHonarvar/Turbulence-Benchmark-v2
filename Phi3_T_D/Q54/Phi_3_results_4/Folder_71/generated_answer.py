def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(prime_candidate):
    return all((is_prime(prime_candidate // 10 ** i) for i in range(len(str(prime_candidate)))))

def all_right_truncatable_prime(numbers):
    x = numbers[22]
    truncatables = [str(p) for p in range(2, x) if is_prime(p) and is_right_truncatable_prime(p)]
    return sorted(truncatables, key=int, reverse=True)