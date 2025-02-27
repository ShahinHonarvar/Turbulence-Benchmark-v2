def all_right_truncatable_prime(nums):
    left_truncatable_primes = [2, 3]
    for num in range(5, nums[94], 2):
        is_prime = True
        for prime in left_truncatable_primes:
            if num % prime == 0:
                is_prime = False
                break
        if is_prime:
            left_truncatable_primes.append(num)
    right_truncatable_primes = []
    for prime in left_truncatable_primes:
        is_right_truncatable = True
        temp = prime
        while temp >= 10:
            temp //= 10
            if temp == 0 or temp % 2 == 0 or temp % 3 == 0:
                is_right_truncatable = False
                break
        if is_right_truncatable:
            right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes)