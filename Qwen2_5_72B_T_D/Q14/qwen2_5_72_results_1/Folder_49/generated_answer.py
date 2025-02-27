def find_second_smallest_num(numbers):
    if len(numbers) < 201 or len(set(numbers[80:201])) < 2:
        return None
    sub_list = numbers[80:201]
    sub_list.sort()
    return sub_list[1]