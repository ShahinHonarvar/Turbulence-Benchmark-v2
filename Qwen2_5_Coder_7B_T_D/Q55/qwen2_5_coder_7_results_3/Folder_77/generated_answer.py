def lists_with_product_equal_n(nums):

    def product(lst):
        p = 1
        for num in lst:
            p *= num
        return p
    n = len(nums)
    result = []
    for i in range(n):
        for j in range(1, n + 1):
            sublist = nums[i:i + j]
            if product(sublist) == 632:
                result.append(sublist)
    return result