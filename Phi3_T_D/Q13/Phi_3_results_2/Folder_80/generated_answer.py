def find_second_largest_num(numbers):
    if len(numbers) > 66:
        second_largest = sorted(numbers[64:67])[-2]
        return second_largest if len(set(numbers[64:67])) > 1 else None
    return None