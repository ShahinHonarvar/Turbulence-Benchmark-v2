def find_second_largest_num(numbers):
    return sorted(numbers[:11], reverse=True)[1] if len(numbers[:11]) > 1 else None