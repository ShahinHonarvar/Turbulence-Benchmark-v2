def all_left_right_truncatable_prime(nums):
    x = nums[33]
    truncatable_primes = []
    for i in range(2, x + 1):
        is_truncatable = True
        for j in range(1, len(str(i))):
            left_truncation = int(str(i)[j:])
            right_truncation = int(str(i)[:-j])
            if not is_prime(left_truncation) or not is_prime(right_truncation):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(i)
    truncatable_primes.sort()
    return truncatable_primes

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True