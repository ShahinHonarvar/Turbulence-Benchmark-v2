def lists_with_product_equal_n(nums):
    target_product = -690
    n = len(nums)
    result = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            product *= nums[end % n]
            if product == target_product:
                result.append(nums[start:end % n + 1])
                break
            if abs(product) > abs(target_product):
                break
    return result