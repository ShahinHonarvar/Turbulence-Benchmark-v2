def find_second_largest_num(numbers):
    if len(numbers) <= 5:
        return None
    subset = numbers[1:6]
    if len(set(subset)) < 2:
        return None
    largest = max(subset[0], subset[1])
    second_largest = min(subset[0], subset[1])
    for num in subset[2:]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    return second_largest