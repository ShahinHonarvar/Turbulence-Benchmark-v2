def lists_with_product_equal_n(nums):

    def find_sublists(nums, target, sublist, start_index):
        for i in range(start_index, len(nums)):
            sublist.append(nums[i])
            product = 1
            for j in sublist:
                product *= j
            if product == target:
                result.append(sublist[:])
            if product < target:
                find_sublists(nums, target, sublist, i + 1)
            sublist.pop()
    result = []
    find_sublists(nums + nums, 45, [], 0)
    return result