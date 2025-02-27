def lists_with_product_equal_n(nums):

    def product(lst):
        p = 1
        for num in lst:
            p *= num
        return p
    n = len(nums)
    result = []
    for start in range(n):
        product_current = 1
        for end in range(start, start + n):
            product_current *= nums[end % n]
            if product_current == -87:
                result.append(nums[start % n:end % n + 1])
    return result