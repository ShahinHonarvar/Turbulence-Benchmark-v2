def find_second_smallest_num(nums):
    start, end = (533, min(len(nums), 605))
    unique_nums = {num for num in nums[start:end + 1]}
    if len(unique_nums) < 2:
        return None
    else:
        return sorted(unique_nums)[1]