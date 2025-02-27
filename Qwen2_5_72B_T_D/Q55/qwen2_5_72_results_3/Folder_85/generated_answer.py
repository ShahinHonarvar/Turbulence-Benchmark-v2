def lists_with_product_equal_n(nums):
    size = len(nums)
    results = []
    target_product = -97
    for start in range(size):
        product = 1
        for end in range(size):
            index = (start + end) % size
            product *= nums[index]
            if product == target_product:
                results.append(nums[start:index + 1])
            if product == 0 or abs(product) > abs(target_product):
                break
    return results