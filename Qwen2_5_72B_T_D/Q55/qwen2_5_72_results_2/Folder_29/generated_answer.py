def lists_with_product_equal_n(nums):
    target_product = 15
    n = len(nums)
    result = []

    def get_product(lst):
        product = 1
        for num in lst:
            product *= num
        return product
    for start in range(n):
        for end in range(1, n + 1):
            sublist = nums[start:start + end] + nums[:end - (n - start)]
            if get_product(sublist) == target_product:
                result.append(sublist)
    return result