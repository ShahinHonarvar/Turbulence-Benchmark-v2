def find_second_largest_num(nums):
    relevant_nums = nums[27:56]
    if len(relevant_nums) < 2:
        return None
    largest = max(relevant_nums[0], relevant_nums[1])
    second_largest = min(relevant_nums[0], relevant_nums[1])
    for num in relevant_nums[2:]:
        if num > largest:
            second_largest, largest = (largest, num)
        elif largest > num > second_largest:
            second_largest = num
    return second_largest