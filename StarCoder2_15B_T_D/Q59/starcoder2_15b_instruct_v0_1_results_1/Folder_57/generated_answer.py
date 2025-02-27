def all_left_truncatable_prime(nums):
    nums_tuple = tuple(nums)
    x = nums_tuple[54]
    left_truncatable_primes = []
    for num in range(2, x):
        is_left_truncatable = True
        for i in range(len(str(num))):
            truncated_num = int(str(num)[i:])
            if not is_prime(truncated_num):
                is_left_truncatable = False
                break
        if is_left_truncatable:
            left_truncatable_primes.append(num)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes