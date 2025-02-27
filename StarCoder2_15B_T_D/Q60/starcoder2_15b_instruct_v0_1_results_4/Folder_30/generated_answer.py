def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    if len(numbers) < 38:
        return []
    x = numbers[37]
    truncatable_primes = []
    for i in range(10, x + 1):
        if is_prime(i):
            truncated_prime = i
            while truncated_prime >= 10:
                if not is_prime(truncated_prime):
                    break
                truncated_prime = int(str(truncated_prime)[1:])
            if truncated_prime in [2, 3, 5, 7]:
                truncatable_primes.append(i)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes