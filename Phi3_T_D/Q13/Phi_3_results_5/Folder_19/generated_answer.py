def find_second_largest_num(nums):
    try:
        second_largest = sorted(nums[3:6], reverse=True)[1]
    except IndexError:
        second_largest = None
    return second_largest