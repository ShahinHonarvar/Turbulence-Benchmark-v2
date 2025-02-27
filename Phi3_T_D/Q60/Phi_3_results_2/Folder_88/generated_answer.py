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

def all_left_right_truncatable_prime(number_range):
    primes = [i for i in range(2, number_range[0]) if is_prime(i)]
    x = number_range[93]
    result = []
    for prime in primes:
        str_prime = str(prime)
        left_truncs = [int(str_prime[i:]) for i in range(len(str_prime))]
        right_truncs = [int(str_prime[:i + 1]) for i in range(len(str_prime))]
        if all((is_prime(t) for t in left_truncs + right_truncs)):
            result.append(prime)
    return result