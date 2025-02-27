def find_second_largest_num(numbers):
    start, end = (3, 5)
    sub_list = numbers[start:end + 1]
    if not sub_list or len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2]