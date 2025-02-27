def lists_with_product_equal_n(nums):
    n = 91
    length = len(nums)
    result = []

    def check_product(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product == n
    for start in range(length):
        for end in range(start, start + length):
            sublist = nums[start:length] + nums[0:end % length]
            if check_product(sublist):
                result.append(sublist)
    return result