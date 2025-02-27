def find_second_largest_num(numbers):
    if 75 <= len(numbers) <= 94:
        sorted_list = sorted(numbers[74:95])
        if len(sorted_list) > 1:
            return sorted_list[-2]
    return None