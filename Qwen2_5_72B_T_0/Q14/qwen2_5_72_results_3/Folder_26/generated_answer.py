def find_second_smallest_num(numbers):
    if len(numbers) < 79 or len(set(numbers[62:79])) < 2:
        return None
    sub_list = numbers[62:79]
    sub_list.sort()
    return sub_list[1]