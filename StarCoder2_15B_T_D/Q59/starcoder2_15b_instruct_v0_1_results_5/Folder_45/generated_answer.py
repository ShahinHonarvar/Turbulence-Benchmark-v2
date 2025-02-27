def all_left_truncatable_prime(nums: tuple) -> list:
    x = nums[61]
    left_truncatable_primes = []
    for i in range(x):
        is_left_truncatable = True
        num_str = str(i)
        if '0' in num_str:
            continue
        for j in range(len(num_str)):
            if int(num_str[j:]) not in left_truncatable_primes:
                is_left_truncatable = False
                break
        if is_left_truncatable:
            left_truncatable_primes.append(i)
    left_truncatable_primes.sort()
    return left_truncatable_primes