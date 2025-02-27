def lists_with_product_equal_n(nums):

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    n = len(nums)
    found_sublists = []
    for start in range(n):
        for end in range(start, n + 1):
            if product(nums[start:end] + nums[:max(0, end - n)]) == -23:
                found_sublists.append(nums[start:end] + nums[:max(0, end - n)])
    return found_sublists