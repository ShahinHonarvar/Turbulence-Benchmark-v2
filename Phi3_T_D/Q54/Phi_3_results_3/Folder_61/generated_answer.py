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
    x = numbers[3]
    primes = [i for i in range(10, x) if is_prime(i)]
    right_truncatable_primes = []
    while primes:
        prime = primes.pop()
        str_prime = str(prime)
        is_truncatable = True
        while str_prime:
            str_prime = str_prime[:-1]
            if not str_prime or not is_prime(int(str_prime)):
                is_truncatable = False
                break
        if is_truncatable:
            right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes, reverse=True)