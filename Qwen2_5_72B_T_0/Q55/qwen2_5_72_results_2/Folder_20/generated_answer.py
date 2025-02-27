def lists_with_product_equal_n(nums):
    n = len(nums)
    nums = nums + nums
    target_product = -69
    result = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            product *= nums[end]
            if product == target_product:
                result.append(nums[start:end + 1])
            elif abs(product) > abs(target_product):
                break
    return result