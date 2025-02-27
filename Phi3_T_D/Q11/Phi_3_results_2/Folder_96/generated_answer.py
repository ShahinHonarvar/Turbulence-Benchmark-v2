def find_largest_num(numbers):
    if len(numbers) > 250:
        largest = max(numbers[50:201])
        return largest
    else:
        return None