def all_right_truncatable_prime(nums):
    x = nums[41]
    primes = set()
    for num in range(2, x):
        if all((int(num) % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            primes.add(num)
    right_truncatable_primes = []
    for prime in primes:
        str_prime = str(prime)
        is_right_truncatable = True
        for i in range(len(str_prime)):
            if int(str_prime[i:]) not in primes:
                is_right_truncatable = False
                break
        if is_right_truncatable:
            right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes, reverse=True)