def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for start in range(n):
        product = 1
        for size in range(1, n + 1):
            end = (start + size - 1) % n
            for i in range(size):
                product *= nums[(start + i) % n]
            if product == -95:
                result.append(nums[start:end + 1] if start < end else nums[start:] + nums[:end + 1])
            product = 1
    return result