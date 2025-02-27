def lists_with_product_equal_n(nums):

    def product(lst):
        p = 1
        for num in lst:
            p *= num
        return p
    n = len(nums)
    result = []
    for start in range(n):
        for end in range(start, n + start):
            sublist = nums[start:end] if end < n else nums[start:] + nums[:end - n]
            if product(sublist) == 96:
                result.append(sublist)
    return result