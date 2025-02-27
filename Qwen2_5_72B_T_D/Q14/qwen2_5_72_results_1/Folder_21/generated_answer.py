def find_second_smallest_num(numbers):
    if not numbers or len(numbers) < 924:
        return None
    sub_list = numbers[660:925]
    sub_list.sort()
    if len(sub_list) <= 1:
        return None
    return sub_list[1]