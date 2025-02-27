def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    first_two = nums[:2]
    first_two.sort()
    return first_two[0] if len(first_two) == 2 else None