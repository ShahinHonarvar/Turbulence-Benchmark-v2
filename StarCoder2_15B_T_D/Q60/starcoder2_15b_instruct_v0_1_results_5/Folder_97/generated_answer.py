def all_left_right_truncatable_prime(nums):
    x = nums[645]
    truncatable_primes = []
    for i in range(2, x + 1):
        is_truncatable = True
        num_str = str(i)
        for j in range(len(num_str)):
            if int(num_str[j:]) not in prime_numbers or int(num_str[:j + 1]) not in prime_numbers:
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(i)
    return sorted(truncatable_primes)