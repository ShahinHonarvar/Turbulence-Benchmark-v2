def lists_with_product_equal_n(nums):
    n = len(nums)

    def product_sublist(start, end):
        product = 1
        for i in range(start, end):
            product *= nums[i % n]
        return product
    result = []
    for start in range(n):
        for length in range(1, n + 1):
            if product_sublist(start, start + length) == -72:
                sublist = nums[start:start + length]
                if length > n // 2:
                    sublist = nums[start:start + length - n]
                result.append(sublist)
    return result