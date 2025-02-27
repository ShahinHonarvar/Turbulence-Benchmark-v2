def lists_with_product_equal_n(nums):
    target_product = -61
    n = len(nums)
    result = []
    for start in range(n):
        product = 1
        for end in range(n):
            actual_end = (start + end) % n
            product *= nums[actual_end]
            if product == target_product:
                result.append(nums[start:actual_end + 1] if actual_end >= start else nums[start:] + nums[:actual_end + 1])
            if product and abs(product) > abs(target_product):
                break
    return result