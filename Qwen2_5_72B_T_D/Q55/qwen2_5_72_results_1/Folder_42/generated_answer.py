def lists_with_product_equal_n(nums):

    def find_sublists(start, target):
        sublists, product = ([], 1)
        for i in range(start, start + len(nums)):
            product *= nums[i % len(nums)]
            if product == target:
                sublists.append(nums[start:i % len(nums) + 1])
            elif product > target:
                break
        return sublists
    result = []
    for i in range(len(nums)):
        result.extend(find_sublists(i, 25))
    return result