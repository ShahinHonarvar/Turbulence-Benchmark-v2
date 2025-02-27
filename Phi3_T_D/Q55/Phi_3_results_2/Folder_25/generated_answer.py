def lists_with_product_equal_n(nums):
    n, result = (-32, [])
    for start in range(len(nums)):
        product = 1
        for end in range(start, start + len(nums)):
            product = product * nums[end % len(nums)]
            if product == n:
                result.append(nums[start:end % len(nums) + 1])
            elif product > n:
                break
    return result