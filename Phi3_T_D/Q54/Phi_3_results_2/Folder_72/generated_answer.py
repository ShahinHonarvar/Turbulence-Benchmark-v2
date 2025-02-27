def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n, primes):
    if n == 0 or n not in primes:
        return False
    return all((not is_prime(int(str(n)[:i])) for i in range(1, len(str(n)))))

def all_right_truncatable_prime(numbers):
    for num in range(2, numbers[31])[::-1]:
        if is_right_truncatable_prime(num, set(filter(is_prime, range(2, numbers[31] + 1)))):
            return [num]
    return []