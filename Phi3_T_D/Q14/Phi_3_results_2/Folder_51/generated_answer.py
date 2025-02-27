def find_second_smallest_num(nums):
    if 1 <= len(nums) <= 8:
        second_smallest = sorted(nums)[1]
        return second_smallest
    return None