def all_left_right_truncatable_prime(nums):
    left_right_truncatable_primes = []
    for num in nums:
        num_str = str(num)
        if '0' in num_str:
            continue
        is_truncatable = True
        for i in range(len(num_str) - 1):
            truncated_num_str = num_str[i + 1:]
            if int(truncated_num_str) % 2 == 0:
                is_truncatable = False
                break
        if is_truncatable:
            left_right_truncatable_primes.append(num)
    left_right_truncatable_primes.sort(reverse=True)
    return left_right_truncatable_primes