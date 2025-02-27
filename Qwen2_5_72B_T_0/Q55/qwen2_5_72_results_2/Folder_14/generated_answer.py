def lists_with_product_equal_n(nums):

    def find_sublists(start, product, length):
        sublists = []
        current_product = 1
        for i in range(length):
            index = (start + i) % len(nums)
            current_product *= nums[index]
            if current_product == product:
                sublists.append(nums[start:start + i + 1] if start + i + 1 <= len(nums) else nums[start:] + nums[:i + 1 - len(nums) + start])
            if current_product == 0:
                break
        return sublists
    result = []
    for i in range(len(nums)):
        result.extend(find_sublists(i, -72, len(nums)))
    return result