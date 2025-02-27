def find_second_largest_num(nums):
    relevant_nums = reversed(sorted(nums[20:201]))
    for num in relevant_nums:
        try:
            return next((n for n in relevant_nums if n != num))
        except StopIteration:
            continue
    return None