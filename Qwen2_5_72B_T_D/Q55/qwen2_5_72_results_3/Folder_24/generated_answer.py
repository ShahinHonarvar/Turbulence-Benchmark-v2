def lists_with_product_equal_n(nums):
    target_product = -89
    n = len(nums)
    result = []
    for start in range(n):
        product = 1
        for length in range(1, n + 1):
            end = (start + length) % n
            product *= nums[end - 1]
            if product == target_product:
                result.append(nums[start:end] if start < end else nums[start:] + nums[:end])
            if product == 0 or abs(product) > abs(target_product):
                break
    return result