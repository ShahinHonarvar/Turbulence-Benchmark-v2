def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[96]
    primes = []
    for num in range(2, x):
        for i in range(len(str(num))):
            if not is_prime(int(str(num)[i:])):
                break
        else:
            primes.append(num)
    primes.sort(reverse=True)
    return primes