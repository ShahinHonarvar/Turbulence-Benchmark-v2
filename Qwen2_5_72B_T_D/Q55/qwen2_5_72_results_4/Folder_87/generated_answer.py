def lists_with_product_equal_n(nums):
    n = 27
    length = len(nums)
    result = []

    def product_of_sublist(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product
    for start in range(length):
        for end in range(start, start + length):
            sublist = nums[start:length] + nums[0:end % length]
            if product_of_sublist(sublist) == n:
                result.append(sublist)
    return result