def find_second_largest_num(list_of_nums):
    list_of_nums.sort(reverse=True)
    if len(list_of_nums) > 100:
        return list_of_nums[10]
    else:
        return None