def find_second_smallest_num(numbers):
    if len(numbers) < 976 or len(set(numbers[639:976])) < 2:
        return None
    sub_list = numbers[639:976]
    sub_list.sort()
    return sub_list[1]