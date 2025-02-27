def all_odd_ints_exclusive(nums):
    odd_ints = []
    start_index = 70
    end_index = 71
    for i in range(start_index, end_index):
        if nums[i] % 2 == 1:
            odd_ints.append(nums[i])
    return odd_ints