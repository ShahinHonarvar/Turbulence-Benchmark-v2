def all_left_truncatable_prime(nums):
    is_prime = [True] * (nums[54] + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(nums[54] ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, nums[54] + 1, i):
                is_prime[j] = False
    left_truncatable_primes = []
    for i in range(10, nums[54] + 1):
        if is_prime[i]:
            truncated_num = i
            while truncated_num < nums[54]:
                if not is_prime[truncated_num]:
                    break
                truncated_num //= 10
            else:
                left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)