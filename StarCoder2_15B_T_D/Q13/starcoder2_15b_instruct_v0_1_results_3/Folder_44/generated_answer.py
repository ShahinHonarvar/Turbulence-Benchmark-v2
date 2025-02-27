def find_second_largest_num(list_of_nums):
    sorted_list = sorted(list_of_nums[13:69], reverse=True)
    return sorted_list[1] if len(sorted_list) > 1 else None