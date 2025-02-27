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

def all_right_truncatable_prime(numbers):
    x = numbers[87]
    primes = [i for i in range(2, x) if is_prime(i)]
    right_truncatable = []
    for prime in primes:
        str_prime = str(prime)
        while len(str_prime) > 1:
            str_prime = str_prime[:-1]
            if not is_prime(int(str_prime)):
                break
        else:
            right_truncatable.append(prime)
    return sorted(right_truncatable)