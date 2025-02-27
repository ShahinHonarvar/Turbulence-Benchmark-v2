def find_second_largest_num(numbers):
    return sorted(numbers[262:747], reverse=True)[1] if len(numbers[262:747]) > 1 else None