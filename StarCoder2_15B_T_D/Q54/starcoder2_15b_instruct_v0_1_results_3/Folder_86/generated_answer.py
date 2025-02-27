import math

def all_right_truncatable_prime(nums):
    """
    Returns the sorted list of all right-truncatable prime numbers less than x,
    where x is the integer at index 126 in `nums`. The returned list is sorted in
    descending order. If there is no such right-truncatable prime number, an empty
    list is returned.
    """
    x = nums[126]
    primes = [True] * x
    primes[0] = False
    primes[1] = False
    for i in range(2, int(math.sqrt(x)) + 1):
        if primes[i]:
            for j in range(i * i, x, i):
                primes[j] = False
    right_truncatable_primes = []
    for i in range(x - 1, 0, -1):
        if primes[i]:
            is_right_truncatable = True
            for j in range(len(str(i)) - 1, 0, -1):
                truncated_num = int(str(i)[:j])
                if not primes[truncated_num]:
                    is_right_truncatable = False
                    break
            if is_right_truncatable:
                right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)