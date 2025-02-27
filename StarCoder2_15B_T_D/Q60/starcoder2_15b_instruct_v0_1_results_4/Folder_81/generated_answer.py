def all_left_right_truncatable_prime(nums):
    left_truncatable = [2, 3, 5, 7]
    right_truncatable = [2, 3, 5, 7]
    x = nums[98]
    for i in range(10, x + 1):
        if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or (i % 7 == 0):
            continue
        is_left_truncatable = True
        is_right_truncatable = True
        num_str = str(i)
        for j in range(1, len(num_str)):
            left_num = int(num_str[j:])
            right_num = int(num_str[:len(num_str) - j])
            if left_num % 2 == 0 or left_num % 3 == 0 or left_num % 5 == 0 or (left_num % 7 == 0):
                is_left_truncatable = False
                break
            if right_num % 2 == 0 or right_num % 3 == 0 or right_num % 5 == 0 or (right_num % 7 == 0):
                is_right_truncatable = False
                break
        if is_left_truncatable:
            left_truncatable.append(i)
        if is_right_truncatable:
            right_truncatable.append(i)
    return sorted(set(left_truncatable).intersection(right_truncatable))