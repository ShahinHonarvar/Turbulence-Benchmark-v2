def lists_with_product_equal_n(nums):
    n = len(nums)
    nums = nums + nums
    result = []
    for start in range(n):
        product = 1
        for length in range(n):
            product *= nums[start + length]
            if product == -7:
                result.append(nums[start:start + length + 1])
            elif abs(product) > 7:
                break
    return result