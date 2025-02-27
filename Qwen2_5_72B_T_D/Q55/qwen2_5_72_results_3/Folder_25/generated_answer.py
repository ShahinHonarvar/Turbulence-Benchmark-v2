def lists_with_product_equal_n(nums):

    def circular_sublists(nums, length):
        for i in range(len(nums)):
            yield nums[i:i + length]
            if i + length < len(nums):
                yield (nums[i:i + length] + nums[:length - (len(nums) - i)])
            else:
                yield (nums[i:] + nums[:i + length - len(nums)])

    def product(lst):
        p = 1
        for num in lst:
            p *= num
        return p
    n = len(nums)
    result = []
    for length in range(1, n + 1):
        for sublist in circular_sublists(nums, length):
            if product(sublist) == -32:
                result.append(sublist)
    return result