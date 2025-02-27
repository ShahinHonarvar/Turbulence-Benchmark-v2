def lists_with_product_equal_n(nums):

    def get_sublists(start, end):
        sublists = []
        product = 1
        for i in range(start, end):
            product *= nums[i]
            if product == 8:
                sublists.append(nums[start:i + 1])
        return sublists
    result = []
    n = len(nums)
    for i in range(n):
        result.extend(get_sublists(i, n))
        result.extend(get_sublists(0, i))
    return result