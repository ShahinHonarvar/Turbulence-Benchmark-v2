def lists_with_product_equal_n(nums):
    n = len(nums)
    nums = nums + nums
    target_product = -115
    result = []
    for start in range(n):
        for end in range(start + 1, start + n + 1):
            if end > 2 * n:
                break
            current_product = 1
            for i in range(start, end):
                current_product *= nums[i]
            if current_product == target_product:
                result.append(nums[start:end])
    return result