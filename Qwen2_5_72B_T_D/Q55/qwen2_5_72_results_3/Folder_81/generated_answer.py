def lists_with_product_equal_n(nums):
    n = len(nums)
    nums = nums + nums
    target_product = -8
    result = []

    def product_of_sublist(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product
    for start in range(n):
        for end in range(start + 1, start + n + 1):
            sublist = nums[start:end]
            if product_of_sublist(sublist) == target_product:
                result.append(sublist)
    return result