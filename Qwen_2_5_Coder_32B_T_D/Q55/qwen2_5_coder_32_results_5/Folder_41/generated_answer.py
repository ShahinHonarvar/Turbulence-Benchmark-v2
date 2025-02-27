def lists_with_product_equal_n(nums):

    def circular_index(i):
        return i % len(nums)
    result = []
    for start in range(len(nums)):
        product = 1
        for end in range(start, start + len(nums)):
            product *= nums[circular_index(end)]
            if product == -20:
                result.append(nums[start:circular_index(end + 1)] + (nums[:circular_index(start)] if end >= start + len(nums) - 1 else []))
    return result