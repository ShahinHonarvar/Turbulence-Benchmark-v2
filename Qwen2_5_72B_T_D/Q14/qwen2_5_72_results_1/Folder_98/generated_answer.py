def find_second_smallest_num(numbers):
    if len(numbers) < 7:
        return None
    sixth_index_number = numbers[6]
    return sixth_index_number if sixth_index_number != min(numbers[6:7]) else None