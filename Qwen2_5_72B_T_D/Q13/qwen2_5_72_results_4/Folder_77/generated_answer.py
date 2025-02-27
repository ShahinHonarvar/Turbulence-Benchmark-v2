def find_second_largest_num(numbers):
    if len(numbers) < 538:
        return None
    sub_list = numbers[527:539]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2]