def all_right_truncatable_prime(nums):
    x = nums[70]
    prime_set = set()
    for num in range(2, x):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            prime_set.add(num)
    right_truncatable_primes = []
    for prime in prime_set:
        while prime > 0:
            if prime not in prime_set:
                break
            prime //= 10
        else:
            right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes)