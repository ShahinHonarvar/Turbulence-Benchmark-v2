def lists_with_product_equal_n(nums):
    target_product = -779
    n = len(nums)
    result = []

    def check_product(start, end):
        product = 1
        for i in range(start, end):
            product *= nums[i % n]
        return product == target_product
    for size in range(1, n + 1):
        for start in range(n):
            end = start + size
            if check_product(start, end):
                result.append(nums[start:end] if end <= n else nums[start:] + nums[:end % n])
    return result