def lists_with_product_equal_n(nums):
    n = len(nums)
    nums = nums + nums
    result = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            product *= nums[end]
            if product == -8:
                result.append(nums[start:end + 1])
            elif abs(product) > 8:
                break
    return result