def find_second_largest_num(numbers):
    if len(numbers) < 58:
        return None
    sub_array = numbers[56:58]
    if len(sub_array) < 2:
        return None
    largest = max(sub_array)
    sub_array.remove(largest)
    return max(sub_array)