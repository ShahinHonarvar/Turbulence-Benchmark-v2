def find_second_smallest_num(numbers):
    relevant_nums = numbers[20:201]
    if len(relevant_nums) < 2:
        return None
    relevant_nums.sort()
    return relevant_nums[1]