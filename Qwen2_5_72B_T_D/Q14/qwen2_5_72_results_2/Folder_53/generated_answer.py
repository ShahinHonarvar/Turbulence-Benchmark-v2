def find_second_smallest_num(numbers):
    if not numbers or len(numbers) < 2 or min(numbers) == max(numbers) or (len(set(numbers[0:101])) < 2):
        return None
    sorted_unique_numbers = sorted(set(numbers[0:101]))
    return sorted_unique_numbers[1]