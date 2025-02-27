def lists_with_product_equal_n(nums):

    def product(lst):
        p = 1
        for x in lst:
            p *= x
        return p
    n = len(nums)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sub_list = nums[start:end % n + 1] if end % n >= start else nums[start:] + nums[:end % n + 1]
            if product(sub_list) == -779:
                result.append(sub_list)
    return result