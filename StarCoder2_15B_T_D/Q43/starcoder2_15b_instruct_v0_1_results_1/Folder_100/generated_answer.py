def find_primes_between_indices(nums):
    sublist = nums[25:63]
    is_prime = [True] * len(sublist)
    for i in range(2, int(len(sublist) ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, len(sublist), i):
                is_prime[j] = False
    return sorted([n for i, n in enumerate(sublist) if is_prime[i]])