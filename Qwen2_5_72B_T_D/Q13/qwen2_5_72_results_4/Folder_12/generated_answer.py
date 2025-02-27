def find_second_largest_num(numbers):
    if len(numbers) < 65 or len(numbers) < 15:
        return None
    sublist = numbers[14:65]
    if len(sublist) < 2:
        return None
    sublist.remove(max(sublist))
    return max(sublist) if sublist else None