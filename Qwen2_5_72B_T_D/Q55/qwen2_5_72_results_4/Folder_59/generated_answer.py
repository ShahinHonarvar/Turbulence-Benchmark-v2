def lists_with_product_equal_n(nums):

    def product(sublist):
        prod = 1
        for num in sublist:
            prod *= num
        return prod
    n = len(nums)
    result = []
    for start in range(n):
        for end in range(n):
            sublist = nums[start:start + end + 1]
            if product(sublist) == -3:
                result.append(sublist)
            if start + end + 1 == n:
                circular_sublist = nums[start:] + nums[:end + 1]
                if product(circular_sublist) == -3:
                    result.append(circular_sublist)
    return result