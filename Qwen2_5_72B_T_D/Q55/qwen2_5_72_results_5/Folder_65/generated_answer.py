def lists_with_product_equal_n(nums):
    n = 46
    length = len(nums)
    result = []
    for start in range(length):
        product = 1
        for end in range(start, start + length):
            index = end % length
            product *= nums[index]
            if product == n:
                result.append(nums[start:index + 1])
            elif product > n:
                break
    return result