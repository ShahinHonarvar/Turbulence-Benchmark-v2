def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[370]
    truncatables = []
    primes = {str(prime) for prime in range(2, x) if is_prime(prime)}
    for number in sorted(primes, reverse=True):
        if all((is_prime(int(number[:i])) for i in range(1, len(number)))):
            truncatables.append(int(number))
            if len(truncatables) == len(set((number[:i] for i in range(1, len(number))))):
                break
    return truncatables if truncatables else []