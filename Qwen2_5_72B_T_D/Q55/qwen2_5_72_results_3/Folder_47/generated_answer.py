def lists_with_product_equal_n(nums):

    def product_of_sublist(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product
    n = len(nums)
    result = []
    for start in range(n):
        for length in range(1, n + 1):
            if length <= n:
                sublist = nums[start:start + length] if start + length <= n else nums[start:] + nums[:start + length - n]
                if product_of_sublist(sublist) == -94:
                    result.append(sublist)
    return result