def lists_with_product_equal_n(nums):
    target_product = 99
    length = len(nums)
    result = []
    for start in range(length):
        product = 1
        for end in range(length):
            current_index = (start + end) % length
            product *= nums[current_index]
            if product == target_product:
                result.append(nums[start:current_index + 1])
            elif product > target_product:
                break
    return result