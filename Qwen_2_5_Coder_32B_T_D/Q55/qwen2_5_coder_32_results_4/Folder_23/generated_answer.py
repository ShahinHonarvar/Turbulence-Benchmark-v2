def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for start in range(n):
        product = 1
        for size in range(1, n + 1):
            index = (start + size - 1) % n
            product *= nums[index]
            if product == -95:
                result.append(nums[start:index + 1] if index >= start else nums[start:] + nums[:index + 1])
    return result