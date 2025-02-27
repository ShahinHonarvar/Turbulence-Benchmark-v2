def lists_with_product_equal_n(nums):
    n = 28
    size = len(nums)
    result = []
    for start in range(size):
        product = 1
        for end in range(size):
            product *= nums[(start + end) % size]
            if product == n:
                result.append(nums[start:(start + end + 1) % size])
            elif product > n:
                break
    return result