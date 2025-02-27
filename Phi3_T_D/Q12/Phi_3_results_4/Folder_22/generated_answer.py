def find_smallest_num(numbers):
    if len(numbers) <= 200:
        return None
    return min(numbers[40:200])