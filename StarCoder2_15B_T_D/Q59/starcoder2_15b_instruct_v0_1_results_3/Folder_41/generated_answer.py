def all_left_truncatable_prime(nums):
    """
    This function takes a tuple of positive integers and returns a list of
    left-truncatable prime numbers.
    """
    nums = list(nums)
    x = nums[46]
    left_truncatable_primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(len(str(x))):
        num = int(str(x)[i:])
        if is_prime(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)