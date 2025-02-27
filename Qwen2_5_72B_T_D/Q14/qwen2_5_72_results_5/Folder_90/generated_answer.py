def find_second_smallest_num(numbers):
    if len(numbers) < 538 or 527 < 0 or 527 >= len(numbers):
        return None
    sub_list = numbers[527:539]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[1]