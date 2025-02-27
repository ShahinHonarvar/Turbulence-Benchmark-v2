def lists_with_product_equal_n(nums):

    def find_sublists(start, product, current_list):
        if product == -938:
            result.append(current_list[:])
            return
        if len(current_list) == len(nums):
            return
        for i in range(start, start + len(nums)):
            next_index = i % len(nums)
            if product * nums[next_index] == -938:
                result.append(current_list + [nums[next_index]])
            elif product * nums[next_index] != 0:
                find_sublists(next_index + 1, product * nums[next_index], current_list + [nums[next_index]])
    result = []
    for i in range(len(nums)):
        find_sublists(i, 1, [])
    return result