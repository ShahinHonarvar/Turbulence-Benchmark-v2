def all_left_truncatable_prime(nums):
    x = nums[73]
    left_truncatable_primes = []
    is_prime = [True] * (x + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(x ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, x + 1, i):
                is_prime[j] = False
    for i in range(2, x):
        if is_prime[i]:
            n = i
            is_left_truncatable = True
            while n > 0:
                if not is_prime[n]:
                    is_left_truncatable = False
                    break
                n //= 10
            if is_left_truncatable:
                left_truncatable_primes.append(i)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes