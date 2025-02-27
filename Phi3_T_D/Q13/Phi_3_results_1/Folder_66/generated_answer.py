def find_second_largest_num(nums):
    selected_numbers = nums[50:55]
    unique_numbers = set(selected_numbers)
    rankings = sorted(unique_numbers)
    try:
        return rankings[-2]
    except IndexError:
        return None