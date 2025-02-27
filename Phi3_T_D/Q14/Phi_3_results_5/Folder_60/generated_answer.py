def find_second_smallest_num(numbers):
    start = 56
    end = 98
    if start >= len(numbers) or end >= len(numbers):
        return None
    sub_list = numbers[start:end + 1]
    if len(set(sub_list)) < 2:
        return None
    return sorted(set(sub_list))[1]