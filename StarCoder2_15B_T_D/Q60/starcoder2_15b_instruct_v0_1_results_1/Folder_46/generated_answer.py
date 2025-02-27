def all_left_right_truncatable_prime(nums):
    x = nums[33]
    truncatable_primes = []
    for prime in range(2, x + 1):
        is_truncatable = True
        for i in range(len(str(prime)) - 1):
            truncated_prime = int(str(prime)[i + 1:])
            if not is_prime(truncated_prime):
                is_truncatable = False
                break
            truncated_prime = int(str(prime)[:len(str(prime)) - i - 1])
            if not is_prime(truncated_prime):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(prime)
    truncatable_primes.sort()
    return truncatable_primes

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True