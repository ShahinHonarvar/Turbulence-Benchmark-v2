def all_left_truncatable_prime(nums):
    x = nums[36]
    primes = [2, 3, 5, 7]
    for num in range(11, x, 2):
        if all((int(num) % i for i in range(3, int(num ** 0.5) + 1, 2))) and '0' not in num:
            primes.append(num)
    left_truncatable_primes = []
    for prime in primes:
        is_left_truncatable = True
        for i in range(len(str(prime))):
            if int(str(prime)[i:]) not in primes:
                is_left_truncatable = False
                break
        if is_left_truncatable:
            left_truncatable_primes.append(int(prime))
    return sorted(left_truncatable_primes)