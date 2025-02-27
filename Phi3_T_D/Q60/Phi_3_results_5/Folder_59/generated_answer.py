def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_primes(numbers):
    x = numbers[84]
    truncatable_primes = [p for p in range(23, min(x, 10 ** 6)) if is_prime(p)]
    result = []

    def is_truncatable(prime):
        s = str(prime)
        return all((is_prime(int(s[i:])) and is_prime(int(s[:i + 1])) for i in range(len(s))))
    for p in truncatable_primes:
        if is_truncatable(p):
            result.append(p)
    result.sort(reverse=True)
    return result if result else []