def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[97]
    truncatable_primes = []
    candidates = [str(i) for i in range(2, x) if is_prime(i)]
    for prime in candidates:
        for i in range(len(prime)):
            truncated_num = int(prime[i:])
            if not is_prime(truncated_num):
                break
        else:
            truncatable_primes.append(int(prime))
    return sorted(truncatable_primes)