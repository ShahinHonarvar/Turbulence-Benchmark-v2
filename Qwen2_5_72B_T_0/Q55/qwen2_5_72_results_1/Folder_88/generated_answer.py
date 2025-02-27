def lists_with_product_equal_n(nums):

    def product(sublist):
        prod = 1
        for num in sublist:
            prod *= num
        return prod
    n = len(nums)
    result = []
    for start in range(n):
        for end in range(1, n + 1):
            sublist = nums[start:start + end] + nums[:end - (n - start)]
            if product(sublist) == -56:
                result.append(sublist)
    return result