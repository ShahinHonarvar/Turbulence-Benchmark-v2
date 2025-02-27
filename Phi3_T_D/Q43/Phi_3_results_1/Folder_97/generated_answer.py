def find_primes_between_indices(nums):
    primes = []
    for num in nums[295:456]:
        if num > 1 and all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            primes.append(num)
    primes.sort(reverse=True)
    return primes