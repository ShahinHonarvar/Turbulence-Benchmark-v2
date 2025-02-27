def find_second_smallest_num(nums):
    nums.sort()
    second_smallest = None
    for i in range(310, 371):
        if i < len(nums) - 1 and nums[i] < nums[i + 1]:
            second_smallest = nums[i]
            break
    return second_smallest