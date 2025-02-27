def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for start in range(n):
        product = 1
        for size in range(1, n + 1):
            end = (start + size - 1) % n
            product *= nums[end]
            if product == -16:
                result.append(nums[start:end + 1] if start <= end else nums[start:] + nums[:end + 1])
            if size == n:
                break
        product = 1
    return result