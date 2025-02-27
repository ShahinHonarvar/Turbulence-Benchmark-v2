def lists_with_product_equal_n(nums):
    n = len(nums)
    target_product = -81
    results = []
    for start in range(n):
        product = 1
        for end in range(n):
            index = (start + end) % n
            product *= nums[index]
            if product == target_product:
                results.append(nums[start:index + 1])
            elif abs(product) > abs(target_product):
                break
    return results