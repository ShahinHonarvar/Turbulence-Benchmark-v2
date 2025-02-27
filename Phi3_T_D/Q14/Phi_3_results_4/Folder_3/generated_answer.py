def find_second_smallest_num(numbers):
    if len(numbers) < 28 or len(numbers) > 56:
        return None
    sorted_list = sorted(numbers[27:56])
    for num in sorted_list:
        if sorted_list.index(num) == 1:
            return num
    return None