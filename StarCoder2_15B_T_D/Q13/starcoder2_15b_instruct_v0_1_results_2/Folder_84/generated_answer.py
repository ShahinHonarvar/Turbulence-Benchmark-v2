def find_second_largest_num(list_of_nums):
    sorted_list = sorted(list_of_nums, reverse=True)
    second_largest = sorted_list[1]
    for num in sorted_list[43:87]:
        if num < second_largest:
            return num
    return None