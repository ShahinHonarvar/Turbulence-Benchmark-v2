def lists_with_product_equal_n(nums):
    target_product = -82
    n = len(nums)
    result = []

    def product_of_sublist(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product
    for start in range(n):
        for end in range(start, n + start):
            sublist = nums[start:end + 1]
            if len(sublist) > n:
                break
            if product_of_sublist(sublist) == target_product:
                result.append(sublist)
    return result