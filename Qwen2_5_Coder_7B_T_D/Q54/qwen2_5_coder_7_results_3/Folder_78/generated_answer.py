def all_right_truncatable_prime(nums):
    x = nums[23]
    primes = []
    for num in range(2, x):
        if all((int(num) % i != 0 for i in range(2, int(int(num) ** 0.5) + 1))):
            primes.append(num)
    right_truncatable_primes = []
    for prime in primes:
        str_prime = str(prime)
        while str_prime:
            if int(str_prime) in primes:
                str_prime = str_prime[:-1]
            else:
                break
        else:
            right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes)