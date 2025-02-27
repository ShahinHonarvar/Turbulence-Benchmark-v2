def lists_with_product_equal_n(nums):
    size = len(nums)
    if size == 0:
        return []
    nums = nums * 2
    result = []
    for start in range(size):
        for end in range(start + 1, start + 1 + size):
            current_product = 1
            for i in range(start, end):
                current_product *= nums[i]
                if abs(current_product) > 33:
                    break
            if current_product == -33:
                result.append(nums[start:end])
    return result