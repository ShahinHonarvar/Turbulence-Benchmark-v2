def all_right_truncatable_prime(nums):
    x = nums[19]
    primes = []
    for num in range(2, x):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))) and all((int(num) % 10 ** i != 0 or all((int(num) % i != 0 for i in range(2, int(int(num) % 10 ** i) ** 0.5) + 1)) for i in range(1, len(str(num))))):
            primes.append(num)
    return sorted(primes)