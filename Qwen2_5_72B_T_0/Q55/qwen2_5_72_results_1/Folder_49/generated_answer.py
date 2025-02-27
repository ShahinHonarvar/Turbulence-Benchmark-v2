def lists_with_product_equal_n(nums):
    n = len(nums)
    target_product = -61
    result = []

    def product_of_sublist(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product
    for start in range(n):
        for end in range(start, start + n):
            sublist = nums[start:] + nums[:end % n]
            if product_of_sublist(sublist) == target_product:
                result.append(sublist)
    return result