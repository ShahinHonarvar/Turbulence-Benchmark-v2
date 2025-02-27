def find_second_largest_num(numbers):
    part_of_list = numbers[52:72]
    if len(set(part_of_list)) < 2:
        return None
    return sorted(set(part_of_list))[-2]