def all_right_truncatable_prime(nums):
    x = nums[38]
    primes = []
    for num in range(2, x):
        if all((int(str(num)[-i:]) in primes for i in range(1, len(str(num)) + 1))) and all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            primes.append(num)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True