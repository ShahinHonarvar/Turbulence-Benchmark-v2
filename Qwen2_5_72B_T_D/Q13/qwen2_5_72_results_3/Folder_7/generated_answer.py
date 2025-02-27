def find_second_largest_num(numbers):
    if len(numbers) < 924 or len(numbers) < 661:
        return None
    sliced_list = numbers[661:925]
    if len(sliced_list) < 2:
        return None
    largest = max(sliced_list[0], sliced_list[1])
    second_largest = min(sliced_list[0], sliced_list[1])
    for num in sliced_list[2:]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    return second_largest