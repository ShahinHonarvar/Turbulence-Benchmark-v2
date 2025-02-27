def find_second_smallest_num(numbers):
    sorted_numbers = sorted(numbers)
    second_smallest = sorted_numbers[70:201][1]
    return second_smallest if 70 <= len(sorted_numbers) - 2 <= 200 else None