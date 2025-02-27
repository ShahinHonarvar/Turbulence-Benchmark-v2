def helper_product(nums, i, temp, target, result):
    if i == len(nums):
        if temp[-1] * nums[0] == target:
            result.append(temp[:])
        return
    helper_product(nums, i + 1, temp, target, result)
    temp.append(nums[i])
    helper_product(nums, i + 1, temp, target, result)
    temp.pop()

def lists_with_product_equal_n(circular_list, target=37):
    if not circular_list:
        return []
    result = []
    helper_product(circular_list, 0, [], target, result)
    return result