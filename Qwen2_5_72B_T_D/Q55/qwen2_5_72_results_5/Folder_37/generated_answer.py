def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    target_product = -76
    for start in range(n):
        product = 1
        for length in range(1, n + 1):
            end = (start + length) % n
            product *= nums[end - 1]
            if product == target_product:
                result.append(nums[start:end] if start < end else nums[start:] + nums[:end])
            if length > 1 and product == 1:
                break
        if product == 0:
            break
    return result