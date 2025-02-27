def lists_with_product_equal_n(nums):

    def match_product(start, end, target):
        prod = 1
        for i in range(start, end + 1):
            prod *= nums[i % len(nums)]
            if prod == target:
                if end - start + 1 == 1:
                    return [nums[start]]
                else:
                    return nums[start:end + 1]
            elif prod > target:
                return None
        return None
    sublists = []
    for i in range(len(nums)):
        sublist = match_product(i, i, 247)
        if sublist:
            sublists.append(sublist)
        for j in range(i + 1, len(nums)):
            sublist = match_product(i, j, 247)
            if sublist:
                sublists.append(sublist)
            if j == len(nums) - 1 and (i == 0 or j == len(nums) - 2):
                break
    return sublists