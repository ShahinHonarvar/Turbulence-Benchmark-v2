def all_right_truncatable_prime(nums):
    """
    Returns a sorted list of all right-truncatable prime numbers in the given tuple of positive integers.
    """
    x = nums[126]
    right_truncatable_primes = []
    for i in range(2, x):
        is_right_truncatable_prime = True
        for j in range(len(str(i)) - 1):
            truncated_num = int(str(i)[:-(j + 1)])
            if not is_prime(truncated_num):
                is_right_truncatable_prime = False
                break
        if is_right_truncatable_prime:
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)

def is_prime(n):
    """
    Returns True if the given number is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True