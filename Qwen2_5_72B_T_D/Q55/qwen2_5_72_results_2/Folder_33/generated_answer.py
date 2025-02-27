def lists_with_product_equal_n(nums):
    n = len(nums)
    target_product = -115
    result = []
    for start in range(n):
        product = 1
        for size in range(1, n + 1):
            end = (start + size) % n
            product *= nums[end - 1]
            if product == target_product:
                result.append(nums[start:end] if start < end else nums[start:] + nums[:end])
            if size >= n or product == 0:
                break
    return result