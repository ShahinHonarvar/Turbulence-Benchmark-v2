def find_second_smallest_num(list_of_nums):
    sorted_list = sorted(list_of_nums)
    second_smallest = sorted_list[1]
    if 28 <= second_smallest <= 38:
        return second_smallest
    return None