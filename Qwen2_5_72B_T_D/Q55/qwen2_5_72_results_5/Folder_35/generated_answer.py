def lists_with_product_equal_n(nums):
    target_product = 83
    n = len(nums)
    result = []
    for start in range(n):
        current_product = 1
        for end in range(start, start + n):
            current_product *= nums[end % n]
            if current_product == target_product:
                result.append(nums[start:end % n + 1])
            elif current_product > target_product:
                break
    return result