def lists_with_product_equal_n(nums):
    target_product = 45
    n = len(nums)
    result = []
    for start in range(n):
        product = 1
        for size in range(1, n + 1):
            end = (start + size) % n
            product *= nums[end - 1]
            if product == target_product:
                result.append(nums[start:end] if end > start else nums[start:] + nums[:end])
            elif product > target_product:
                break
    return result