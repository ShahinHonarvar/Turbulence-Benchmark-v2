def find_second_largest_num(nums):
    if len(nums) < 538 or nums[527:539] == []:
        return None
    sublist = nums[527:539]
    sublist.sort()
    return sublist[-2]