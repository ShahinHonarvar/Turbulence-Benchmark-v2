def lists_with_product_equal_n(nums):
    target_product = 714
    n = len(nums)
    result = []

    def product_of_sublist(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product
    for start in range(n):
        for end in range(1, n + 1):
            sublist = nums[start:start + end] + nums[:end - (n - start)]
            if product_of_sublist(sublist) == target_product:
                result.append(sublist)
    return result