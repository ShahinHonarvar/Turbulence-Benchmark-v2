def find_second_largest_num(numbers):
    if len(numbers) < 6:
        return None
    sorted_list = sorted(numbers[:6], reverse=True)
    for i in range(1, len(sorted_list)):
        if sorted_list[i] != sorted_list[i - 1]:
            return sorted_list[i]
    return None