def lists_with_product_equal_n(nums):
    n = len(nums)
    nums = nums + nums
    result = []
    target_product = -8
    for start in range(n):
        current_product = 1
        for end in range(start, start + n):
            current_product *= nums[end]
            if current_product == target_product:
                result.append(nums[start:end + 1])
            elif current_product and abs(current_product) > abs(target_product):
                break
    return result