def lists_with_product_equal_n(nums):

    def get_product(lst):
        product = 1
        for num in lst:
            product *= num
        return product
    n = len(nums)
    result = []
    for start in range(n):
        for end in range(start + 1, start + n + 1):
            sublist = nums[start:end] if end <= n else nums[start:] + nums[:end - n]
            if get_product(sublist) == -95:
                result.append(sublist)
    return result