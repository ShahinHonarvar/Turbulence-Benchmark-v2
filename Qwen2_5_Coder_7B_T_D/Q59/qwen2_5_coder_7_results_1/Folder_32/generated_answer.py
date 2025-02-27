def all_left_truncatable_prime(nums):
    x = nums[42]
    primes = []
    for num in range(2, x):
        if all((int(num[:i + 1]) > 0 and all((int(num[:i + 1]) % j != 0 for j in range(2, int(num[:i + 1]) + 1))) for i in range(len(num)))):
            primes.append(num)
    return sorted(primes)