def find_second_largest_num(list_of_nums):
    sorted_list = sorted(list_of_nums, reverse=True)
    second_largest = sorted_list[1]
    return second_largest if 3 <= list_of_nums.index(second_largest) <= 5 else None