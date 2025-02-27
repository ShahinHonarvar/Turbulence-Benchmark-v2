def find_second_smallest_num(numbers):
    if len(numbers) < 538 or numbers[527:539] == []:
        return None
    sub_list = numbers[527:539]
    sub_list.sort()
    return sub_list[1] if len(sub_list) > 1 else None