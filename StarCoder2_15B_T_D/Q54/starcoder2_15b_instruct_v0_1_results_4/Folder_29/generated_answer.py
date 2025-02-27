def is_prime(n):
    if n < 2:
        return False
    sieve = [True] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return sieve[n]

def all_right_truncatable_prime(numbers):
    right_truncatable_primes = []
    for number in numbers:
        if is_prime(number):
            truncated_number = number // 10
            while truncated_number >= 10:
                if not is_prime(truncated_number):
                    break
                truncated_number //= 10
            if truncated_number < 10:
                right_truncatable_primes.append(number)
    return sorted(right_truncatable_primes, reverse=True)