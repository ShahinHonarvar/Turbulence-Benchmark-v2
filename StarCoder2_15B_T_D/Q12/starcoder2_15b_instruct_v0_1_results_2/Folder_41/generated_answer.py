def find_smallest_num(nums):
    start_index = 4
    end_index = 4
    smallest_num = nums[start_index]
    for i in range(start_index, end_index + 1):
        if nums[i] < smallest_num:
            smallest_num = nums[i]
    return smallest_num