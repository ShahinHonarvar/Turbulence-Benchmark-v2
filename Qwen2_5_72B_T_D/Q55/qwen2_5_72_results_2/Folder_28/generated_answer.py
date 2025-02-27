def lists_with_product_equal_n(nums):

    def sublists_with_target_product(start, product, target, length):
        sublists = []
        temp_product = 1
        for i in range(length):
            index = (start + i) % length
            temp_product *= nums[index]
            if temp_product == target:
                sublists.append(nums[start:index + 1])
            elif temp_product > target:
                break
        return sublists
    result = []
    target = 85
    n = len(nums)
    for i in range(n):
        result.extend(sublists_with_target_product(i, 1, target, n))
    return result