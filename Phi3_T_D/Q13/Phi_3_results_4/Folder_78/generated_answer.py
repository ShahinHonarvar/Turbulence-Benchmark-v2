def find_second_largest_num(numbers):
    if 43 <= len(numbers) <= 51:
        sub_list = sorted(numbers[42:52])
        if len(sub_list) > 1:
            return sub_list[-2]
        else:
            return None
    else:
        return None