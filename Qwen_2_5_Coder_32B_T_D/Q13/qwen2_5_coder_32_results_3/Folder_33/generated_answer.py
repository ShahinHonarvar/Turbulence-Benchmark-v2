def find_second_largest_num(numbers):
    if len(numbers) < 775:
        return None
    sublist = numbers[667:775]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(sublist, reverse=True)
    return sorted_sublist[1]