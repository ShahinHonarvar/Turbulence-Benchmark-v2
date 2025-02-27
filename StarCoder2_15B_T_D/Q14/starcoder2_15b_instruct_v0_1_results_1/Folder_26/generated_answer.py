def find_second_smallest_num(numbers):
    sorted_list = sorted(numbers)
    second_smallest = sorted_list[62:79]
    if len(second_smallest) < 2:
        return None
    return sorted(second_smallest)[1]