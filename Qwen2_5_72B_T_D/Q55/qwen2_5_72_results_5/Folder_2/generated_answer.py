def lists_with_product_equal_n(nums):
    target_product = -968
    n = len(nums)
    results = []
    for start in range(n):
        product = 1
        for end in range(n):
            actual_end = (start + end) % n
            product *= nums[actual_end]
            if product == target_product:
                results.append(nums[start:actual_end + 1] if start <= actual_end else nums[start:] + nums[:actual_end + 1])
            if product == 0 or abs(product) > abs(target_product):
                break
    return results