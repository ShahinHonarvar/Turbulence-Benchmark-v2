def find_primes_between_indices(nums):
    result = []
    for i in range(28, 84):
        is_prime = True
        for j in range(2, int(nums[i] ** 0.5) + 1):
            if nums[i] % j == 0:
                is_prime = False
                break
        if is_prime:
            result.append(nums[i])
    return sorted(result)