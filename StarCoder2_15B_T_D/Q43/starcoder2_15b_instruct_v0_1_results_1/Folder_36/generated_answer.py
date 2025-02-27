def find_primes_between_indices(nums):
    is_prime = [True] * (max(nums) + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(max(nums) ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max(nums) + 1, i):
                is_prime[j] = False
    primes = [num for num in nums if is_prime[num] and 229 <= nums.index(num) <= 850]
    return sorted(primes, reverse=True)