def find_second_largest_num(nums):
    second_largest = None
    start_index, end_index = (min(29, len(nums)), min(51, len(nums)))
    for i in range(end_index, start_index - 1, -1):
        if nums[i] != nums[i - 1]:
            if second_largest is None or nums[i] < nums[i - 1]:
                second_largest = nums[i]
            break
    return second_largest