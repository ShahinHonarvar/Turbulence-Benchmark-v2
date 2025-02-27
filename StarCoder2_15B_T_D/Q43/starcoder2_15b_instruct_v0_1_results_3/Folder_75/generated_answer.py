import math

def find_primes_between_indices(nums):
    primes = []
    for i in range(46, 62):
        is_prime = True
        num = nums[i]
        if num < 2:
            continue
        for j in range(2, int(math.sqrt(num)) + 1):
            if num % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    primes.sort()
    return primes