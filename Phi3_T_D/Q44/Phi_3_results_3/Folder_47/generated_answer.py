from itertools import compress

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def composite_nums_between_indices(nums):
    indices = range(75, 89)
    composites = set(compress(nums, map(lambda x: not is_prime(x), nums)))
    return set((nums[i] for i in indices if nums[i] in composites))