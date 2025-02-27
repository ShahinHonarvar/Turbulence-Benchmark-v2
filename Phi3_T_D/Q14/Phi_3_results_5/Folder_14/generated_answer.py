def find_second_smallest_num(nums):
    try:
        second_smallest = sorted(nums[8:10])[1]
        return second_smallest
    except IndexError:
        return None