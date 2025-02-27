def find_second_largest_num(numbers):
    if len(numbers) < 7:
        return None
    sliced_list = numbers[64:67]
    return sorted(sliced_list)[-2] if len(sliced_list) >= 2 else None