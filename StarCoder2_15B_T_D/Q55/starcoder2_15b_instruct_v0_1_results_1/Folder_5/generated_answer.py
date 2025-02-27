def lists_with_product_equal_n(nums):
    result = []
    window_size = 1
    product = 1
    left = 0
    right = 0
    while right < len(nums):
        product *= nums[right]
        while product > -33:
            if product == -33:
                result.append(nums[left:right + 1])
            product /= nums[left]
            left += 1
        right += 1
    return result