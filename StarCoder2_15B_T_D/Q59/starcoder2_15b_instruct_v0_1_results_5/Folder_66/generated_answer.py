def all_left_truncatable_prime(nums):
    x = nums[25]
    result = []
    for i in range(2, x):
        is_left_truncatable = True
        num_str = str(i)
        for j in range(len(num_str)):
            truncated_num_str = num_str[j:]
            if int(truncated_num_str) < 2 or any((int(truncated_num_str) % k == 0 for k in range(2, int(truncated_num_str) // 2 + 1))):
                is_left_truncatable = False
                break
        if is_left_truncatable:
            result.append(i)
    return sorted(result, reverse=True)