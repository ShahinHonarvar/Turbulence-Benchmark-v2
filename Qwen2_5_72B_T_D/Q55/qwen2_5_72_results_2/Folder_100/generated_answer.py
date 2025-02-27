def lists_with_product_equal_n(nums):
    n = len(nums)
    nums *= 2
    result = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            product *= nums[end]
            if product == 48:
                result.append(nums[start:end + 1])
            elif product > 48:
                break
    return result