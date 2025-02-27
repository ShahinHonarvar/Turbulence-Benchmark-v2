from itertools import permutations

def all_right_truncatable_prime(nums):
    x = nums[835]
    right_truncatable_primes = []
    for i in range(1, len(str(x))):
        for permutation in permutations(str(x), i):
            number = int(''.join(permutation))
            if is_prime(number):
                right_truncatable_primes.append(number)
    return sorted(right_truncatable_primes)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True