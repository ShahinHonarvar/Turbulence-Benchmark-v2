def find_second_smallest_num(list_of_nums):
    sorted_list = sorted(list_of_nums[686:988])
    if len(sorted_list) >= 2:
        return sorted_list[1]
    else:
        return None