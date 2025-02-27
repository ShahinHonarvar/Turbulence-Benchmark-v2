def find_second_smallest_num(numbers):
    if len(numbers) < 8:
        return None
    sublist = numbers[1:9]
    sorted_sublist = sorted(sublist)
    return sorted_sublist[1]