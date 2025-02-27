def lists_with_product_equal_n(nums):
    target_product = -46
    n = len(nums)
    results = []
    for start in range(n):
        product = 1
        for end in range(n):
            index = (start + end) % n
            product *= nums[index]
            if product == target_product:
                results.append(nums[start:index + 1])
            if abs(product) > abs(target_product):
                break
    return results