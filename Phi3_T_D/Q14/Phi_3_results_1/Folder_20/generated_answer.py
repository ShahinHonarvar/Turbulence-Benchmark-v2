def find_second_smallest_num(numbers):
    start, end = (len(numbers) - 89, len(numbers) - 66)
    if start > end:
        return None

    def second_smallest(sorted_numbers):
        return None if len(sorted_numbers) < 2 else sorted_numbers[1]
    return second_smallest(sorted(numbers[start:end + 1]))