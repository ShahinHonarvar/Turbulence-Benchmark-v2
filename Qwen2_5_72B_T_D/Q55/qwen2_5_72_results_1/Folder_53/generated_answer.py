def lists_with_product_equal_n(nums):
    n = len(nums)
    target_product = -87
    result = []
    for start in range(n):
        product = 1
        for end in range(n):
            actual_end = (start + end) % n
            product *= nums[actual_end]
            if product == target_product:
                result.append(nums[start:actual_end + 1] if start <= actual_end else nums[start:] + nums[:actual_end + 1])
            if abs(product) > abs(target_product):
                break
    return result