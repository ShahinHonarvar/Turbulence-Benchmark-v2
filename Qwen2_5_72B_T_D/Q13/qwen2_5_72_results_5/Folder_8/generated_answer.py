def find_second_largest_num(numbers):
    if len(numbers) > 23:
        sliced_list = numbers[23:24]
        if len(sliced_list) == 1:
            return None
        else:
            return sorted(sliced_list)[-2]
    else:
        return None