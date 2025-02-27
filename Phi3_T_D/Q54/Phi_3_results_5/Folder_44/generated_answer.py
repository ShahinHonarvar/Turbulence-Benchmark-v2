def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def truncatable_primes(n):
    primes = [str(i) for i in range(2, n) if is_prime(i)]
    truncatable_list = []
    for prime in primes:
        for i in range(len(prime)):
            if not is_prime(int(prime[i:])):
                break
        else:
            truncatable_list.append(prime)
    return truncatable_list

def all_right_truncatable_prime(numbers):
    x = numbers[39]
    return sorted([int(prime) for prime in truncatable_primes(x)])