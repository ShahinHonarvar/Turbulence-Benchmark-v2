def find_second_smallest_num(numbers):
    if len(numbers) < 976 or len(set(numbers)) != len(numbers):
        return None
    sub_list = numbers[639:976]
    sub_list.sort()
    return sub_list[1] if len(sub_list) > 1 else None