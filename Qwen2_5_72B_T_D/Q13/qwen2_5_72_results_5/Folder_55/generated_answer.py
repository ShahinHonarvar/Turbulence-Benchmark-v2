def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    top_two = sorted(nums[:11], reverse=True)[:2]
    if len(top_two) < 2:
        return None
    return top_two[1]