def lists_with_product_equal_n(nums):

    def circular_slice(lst, start, size):
        return [lst[(start + i) % len(lst)] for i in range(size)]
    result = []
    n = len(nums)
    for size in range(1, n + 1):
        for start in range(n):
            sublist = circular_slice(nums, start, size)
            product = 1
            for num in sublist:
                product *= num
            if product == -17:
                result.append(sublist)
    return result