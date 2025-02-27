def all_right_truncatable_prime(nums):
    x = nums[39]
    truncatable_primes = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            truncated_num = i
            while truncated_num < x:
                is_truncatable_prime = True
                for k in range(2, truncated_num):
                    if truncated_num % k == 0:
                        is_truncatable_prime = False
                        break
                if is_truncatable_prime:
                    truncatable_primes.append(truncated_num)
                truncated_num = truncated_num // 10
    truncatable_primes.sort()
    return truncatable_primes