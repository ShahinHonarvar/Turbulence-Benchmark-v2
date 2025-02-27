def find_second_largest_num(nums):
    sublist = nums[27:56]
    if len(sublist) < 2 or any((n == max(sublist) for n in sublist)):
        return None
    else:
        sublist.sort()
        return sublist[-2]