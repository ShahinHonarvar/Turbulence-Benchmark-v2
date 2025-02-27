def all_left_right_truncatable_prime(nums):
    x = nums[630]
    truncatable_primes = []
    for num in range(2, x + 1):
        if '0' not in str(num):
            is_truncatable = True
            for i in range(1, len(str(num))):
                left_trunc = int(str(num)[i:])
                right_trunc = int(str(num)[:-i])
                if left_trunc % 2 == 0 or right_trunc % 2 == 0:
                    is_truncatable = False
                    break
            if is_truncatable:
                truncatable_primes.append(num)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes